from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView
from core.models import App
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class HomeView(TemplateView):

    template_name = "home.html"


@method_decorator(login_required, name='dispatch')
class DashboardView(ListView):

    template_name = "dashboard.html"
    context_object_name = 'apps'
    queryset = App.objects.all()


@method_decorator(login_required, name='dispatch')
class AppView(DetailView):

    template_name = "app.html"
    model = App

    def get_context_data(self,  **kwargs):
        ctx = super(AppView, self).get_context_data( **kwargs)
        return ctx