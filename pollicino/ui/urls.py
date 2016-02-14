from django.conf.urls import url, include
from .views import HomeView, DashboardView, AppView, AppCreateView, PushConfigurationEdit, PushConfigurationCreate

urlpatterns = [
    url(r'^$', HomeView.as_view(), name="home"),
    url(r'^dashboard/$', DashboardView.as_view(), name="dashboard"),
    url(r'^app/(?P<pk>[-\w]+)/$', AppView.as_view(), name='app-detail'),
    url(r'^new-app/$', AppCreateView.as_view(), name='app-create'),
    url(r'^app-pushconfig-edit/(?P<app_pk>[-\w]+)/$', PushConfigurationEdit.as_view(), name='app-pushconfig-edit'),
    url(r'^app-pushconfig-create/(?P<app_pk>[-\w]+)/$', PushConfigurationCreate.as_view(), name='app-pushconfig-create'),
    url(r'^accounts/', include('authtools.urls')),
    
]
