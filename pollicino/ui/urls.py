from django.conf.urls import url, include
from .views import HomeView, DashboardView, AppView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name="home"),
    url(r'^dashboard/$', DashboardView.as_view(), name="dashboard"),
    url(r'^app/(?P<pk>[-\w]+)/$', AppView.as_view(), name='app-detail'),
    url(r'^accounts/', include('authtools.urls')),
    
]
