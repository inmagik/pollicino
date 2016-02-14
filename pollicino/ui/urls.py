from django.conf.urls import url, include
from .views import  ( HomeView, DashboardView, AppView, AppCreateView, 
    PushConfigurationEdit, PushConfigurationCreate, PushNotifications,
    NotificationMessageCreate, NotificationMessageUpdate )

urlpatterns = [
    url(r'^$', HomeView.as_view(), name="home"),
    url(r'^dashboard/$', DashboardView.as_view(), name="dashboard"),
    url(r'^app/(?P<pk>[-\w]+)/$', AppView.as_view(), name='app-detail'),
    url(r'^new-app/$', AppCreateView.as_view(), name='app-create'),
    url(r'^app-pushconfig-edit/(?P<app_pk>[-\w]+)/$', PushConfigurationEdit.as_view(), name='app-pushconfig-edit'),
    url(r'^app-pushconfig-create/(?P<app_pk>[-\w]+)/$', PushConfigurationCreate.as_view(), name='app-pushconfig-create'),

    #notifications
    url(r'^app-notifications/(?P<app_pk>[-\w]+)/$', PushNotifications.as_view(), name='app-notifications'),
    url(r'^app-notifications-create/(?P<app_pk>[-\w]+)/$', NotificationMessageCreate.as_view(), name='app-notifications-create'),
    url(r'^app-notifications-detail/(?P<app_pk>[-\w]+)/(?P<pk>[-\w]+)/$', NotificationMessageUpdate.as_view(), name='app-notifications-detail'),

    url(r'^accounts/', include('authtools.urls')),
    
]
