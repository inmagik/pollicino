from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView, CreateView, UpdateView

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.forms import ModelForm
#from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

#UserModel = get_user_model()

from core.models import App
from notifications.models import PushConfiguration

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


class AppCreateForm(ModelForm):
    class Meta:
        model = App
        fields = ['name']


@method_decorator(login_required, name='dispatch')
class AppCreateView(CreateView):

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


@method_decorator(login_required, name='dispatch')
class PushConfigurationEdit(HasAppPk, UpdateView):

    template_name = "app_push_update.html"
    model = PushConfiguration
    form_class = PushConfigurationForm

    def get_object(self):
        app = App.objects.get(pk = self.kwargs['app_pk'])
        return app.push_configuration

    def get_success_url(self):
        rvs = reverse('app-detail', args=(self.object.app.id,))
        return rvs


@method_decorator(login_required, name='dispatch')
class PushConfigurationCreate(HasAppPk, CreateView):

    template_name = "app_push_update.html"
    model = PushConfiguration
    form_class = PushConfigurationForm

    def form_valid(self, form):
        app = app.objects.get(pk=self.kwargs['app_pk'])
        candidate = form.save(commit=False)
        candidate.app = app
        candidate.save()
        rvs = reverse('app-detail', args=(app.id,))
        return HttpResponseRedirect(rvs)


    def get_success_url(self):
        rvs = reverse('app-detail', args=(self.object.app.id,))
        return rvs
    