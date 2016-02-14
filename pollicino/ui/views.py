from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView, CreateView, UpdateView, View

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.forms import ModelForm
#from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

#UserModel = get_user_model()

from core.models import App
from notifications.models import PushConfiguration, NotificationMessage


class LoginRequiredView(object):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredView, self).dispatch(request, *args, **kwargs)


class HomeView(TemplateView):
    template_name = "home.html"


class DashboardView(LoginRequiredView, ListView):

    template_name = "dashboard.html"
    context_object_name = 'apps'
    queryset = App.objects.all()


class AppView(LoginRequiredView, DetailView):

    template_name = "app.html"
    model = App

    def get_context_data(self,  **kwargs):
        ctx = super(AppView, self).get_context_data( **kwargs)
        return ctx


class AppCreateForm(ModelForm):
    class Meta:
        model = App
        fields = ['name']


class AppCreateView(LoginRequiredView, CreateView):

    template_name = "app_create.html"
    model = App
    form_class = AppCreateForm

    def get_context_data(self,  **kwargs):
        ctx = super(AppCreateView, self).get_context_data( **kwargs)
        return ctx

    
    def form_valid(self, form):
        candidate = form.save(commit=False)
        candidate.owner = self.request.user  # use your own profile here
        candidate.save()
        rvs = reverse('app-detail', args=(candidate.id,))
        return HttpResponseRedirect(rvs)



class PushConfigurationForm(ModelForm):
    class Meta:
        model = PushConfiguration
        exclude = ['app']


class HasAppPk(object):
    def get_context_data(self, **kwargs):
        ctx = super(HasAppPk, self).get_context_data( **kwargs)
        if 'app_pk' in self.kwargs:
            ctx['app'] = App.objects.get(pk = self.kwargs['app_pk'])
        return ctx


class PushConfigurationEdit(LoginRequiredView, HasAppPk, UpdateView):

    template_name = "app_push_update.html"
    model = PushConfiguration
    form_class = PushConfigurationForm

    def get_object(self):
        app = App.objects.get(pk = self.kwargs['app_pk'])
        return app.push_configuration

    def get_success_url(self):
        rvs = reverse('app-detail', args=(self.object.app.id,))
        return rvs


class PushConfigurationCreate(LoginRequiredView, HasAppPk, CreateView):

    template_name = "app_push_update.html"
    model = PushConfiguration
    form_class = PushConfigurationForm

    def form_valid(self, form):
        app = App.objects.get(pk=self.kwargs['app_pk'])
        candidate = form.save(commit=False)
        candidate.app = app
        candidate.save()
        rvs = reverse('app-detail', args=(app.id,))
        return HttpResponseRedirect(rvs)


    def get_success_url(self):
        rvs = reverse('app-detail', args=(self.object.app.id,))
        return rvs


class PushNotifications(LoginRequiredView, HasAppPk, ListView):

    template_name = "notifications.html"
    queryset = NotificationMessage.objects.all()
    


class NotificationMessageForm(ModelForm):
    class Meta:
        model = NotificationMessage
        fields = ['alert']    

class NotificationMessageUpdateForm(ModelForm):
    class Meta:
        model = NotificationMessage
        fields = ['alert', 'send']    


class NotificationMessageCreate(LoginRequiredView, HasAppPk, CreateView):

    template_name = "notification_create.html"
    model = NotificationMessage
    form_class = NotificationMessageForm

    def form_valid(self, form):
        app = App.objects.get(pk=self.kwargs['app_pk'])
        candidate = form.save(commit=False)
        candidate.app = app
        candidate.save()
        rvs = reverse('app-notifications-detail', args=(app.id, candidate.pk))
        return HttpResponseRedirect(rvs)


class NotificationMessageUpdate(LoginRequiredView, HasAppPk, UpdateView):

    template_name = "notification_update.html"
    model = NotificationMessage
    form_class = NotificationMessageUpdateForm

    def form_valid(self, form):
        app = App.objects.get(pk=self.kwargs['app_pk'])
        candidate = form.save(commit=False)
        #candidate.app = app
        candidate.save()
        rvs = reverse('app-notifications-detail', args=(app.id, candidate.pk))
        return HttpResponseRedirect(rvs)

