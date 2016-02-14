from django.conf.urls import url, include
from .views import HomeView, DashboardView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name="home"),
    url(r'^dashboard/$', DashboardView.as_view(), name="dashboard"),
    url(r'^accounts/', include('authtools.urls')),
]
