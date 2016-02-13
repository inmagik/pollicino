from __future__ import unicode_literals

import time
from django.db import models
from django.core.validators import MaxValueValidator

import core.models as core_models
from apns import APNs, Frame, Payload




class PushConfiguration(models.Model):
    app = models.OneToOneField(core_models.App)
    
    apns_certificate = models.FileField(null=True, upload_to="apns_certificates")
    apns_certificate_dev = models.FileField(null=True, upload_to="apns_certificates_dev")
    
    gcm_api_key = models.CharField(max_length=200, null=True, blank=True)
    use_sandbox = models.BooleanField(default=True) 

    apns_port = '2195'
    gcm_post_url = 'https://android.googleapis.com/gcm/send'
    gcm_max_recipients = models.PositiveSmallIntegerField(default=1000, validators=[MaxValueValidator(1000)])


    def __unicode__(self):
        return self.app


    @property
    def apns_host(self):
        if self.debug_mode:
            return 'gateway.sandbox.push.apple.com'
        return 'gateway.push.apple.com'


    @property
    def current_cert_file(self):
        if self.use_sandbox:
            cert_file = self.apns_certificate_dev
        else:
            cert_file = self.apns_certificate

        if not cert_file:
            raise ValueError("No valid certificate for app")

        return cert_file.path


    def send_notification_apns(self, device_token, payload,identifier=None, expiry=None):
        print "sending notification!", device_token, payload
        apns = APNs(use_sandbox=self.use_sandbox, cert_file=self.current_cert_file)
        return apns.gateway_server.send_notification(device_token, payload, 
            identifier=identifier, expiry=expiry)


    def send_notifications_apns(self, device_tokens, payload, priority=10, 
        identifier=None, expiry=None):

        if not device_tokens:
            raise ValueError("No device tokens specified, should be a list")
        
        apns = APNs(use_sandbox=self.use_sandbox, cert_file=self.current_cert_file)

        # Send multiple notifications in a single transmission
        frame = Frame()
        
        for device_token in device_tokens:
            frame.add_item(device_token, payload, identifier, expiry, priority)
        
        return apns.gateway_server.send_notification_multiple(frame)



    def send_notification_gcm(self, device_token, payload):
        pass


    def send_notifications_gcm(self, device_tokens, payload, priority=10, 
        identifier=None, expiry=None):
        pass



    def get_feedback_apns(self):
        """
        Apple recommends to query the feedback service daily to get the list of device
        tokens. You need to create a new connection to APNS to see all the tokens that 
        have failed since you only receive that information upon connection. 
        Remember, once you have viewed the list of tokens, Apple will clear the list 
        from their servers. Use the timestamp to verify that the device tokens haven't 
        been reregistered since the feedback entry was generated.
        For each device that has not been reregistered, stop sending notifications. 
        By using this information to stop sending push notifications that will fail 
        to be delivered, you reduce unnecessary message overhead and improve overall 
        system performance.
        """
        
        feedback_connection = APNs(use_sandbox=self.use_sandbox, cert_file=self.current_cert_file)
        for (device_token, fail_time) in feedback_connection.feedback_server.items():
            DeviceFeedBack.objects.create(device_token=device_token, fail_time=fail_time, use_sandbox=self.use_sandbox)



class DeviceFeedBack(models.Model):
    """
    Tracks failed notifications for APNS.
    Will be used to cleanup installations or just as a lookup
    """
    app = models.ForeignKey(core_models.App)
    device_token = models.CharField(max_length=200)
    fail_time =  models.DateTimeField()
    use_sandbox = models.BooleanField() 




class InstallationQuerySet(models.QuerySet):
    """
    custom queryset that adds send_notifications method
    """
    #TODO ! USE SENDING MULTIPLE NOTIFICATIONS!
    def send_notifications(self, payload, identifier=None, expiry=None):
        for item in self:
            item.send_notification(payload, identifier=None, expiry=None)

class InstallationManager(models.Manager):
    """
    Custom manager to use InstallationQuerySet and related methods
    """
    def get_queryset(self):
        return InstallationQuerySet(self.model, using=self._db)


class Installation(models.Model):
    """
    Single installation
    """
    app = models.ForeignKey(core_models.App)
    # device_id is an identifier that comes from the device, via OS API
    device_token = models.CharField(max_length=200) 
    # registration_id comes from registration action on the push service provider
    # not sure if needed
    registration_id = models.CharField(max_length=200, unique=True, blank=True, null=True) 
    platform = models.CharField(max_length=200)
    updated_at = models.DateTimeField(auto_now=True)
    app_version = models.CharField(max_length=200, null=True, blank=True)

    #current app locale, for future i18n
    locale = models.CharField(max_length=200, null=True, blank=True)

    #TODO: we will add a nullable reference to app users ...
    # user = ...

    objects = InstallationManager()

    def __unicode__(self):
        return u"%s - %s" % (self.app.pk, self.device_token)


    def send_notification(self, payload, identifier=None, expiry=None):
        cfg = PushConfiguration.objects.get(app=self.app)
        if not cfg:
            raise ValueError("No push configuration for app %s" % app)
        
        if self.platform.upper() == 'IOS':
            return cfg.send_notification_apns(self.device_token, payload, 
                identifier=identifier, expiry=expiry)


        raise ValueError("No push available for platform %s" % self.platform)    


    
# TODO: probably when a new installation is inserted and is present into DeviceFeedBack
# it should be removed (SIGNAL)




class NotificationMessage(models.Model):
    """
    Class for sending a message from the admin.
    when sent will be flagged (cannot resend).
    Send to all devices

    For now it handles "plain" notifications (text, badge and simple alert only)
    """
    app = models.ForeignKey(core_models.App)
    badge = models.IntegerField(null=True, blank=True, default=0)
    sound = models.CharField(max_length=200, null=True, blank=True, default='default')
    alert = models.TextField()
    send = models.BooleanField()

    sent = models.BooleanField(editable=False, default=False    )


    def save(self, *args, **kwargs):
        if self.send and not self.sent:
            installations = Installation.objects.filter(app=self.app)
            payload = Payload(alert=self.alert, sound=self.sound or None, badge=self.badge)
            installations.send_notifications(payload, identifier=self.pk)
            self.sent = True


        return super(NotificationMessage, self).save(*args, **kwargs)




