from django.shortcuts import render
from django.views.generic import View
#from django.contrib.auth.mixins import LoginRequiredMixin
#from rpgine_core.mixins.LoginRequiredMixin import LoginRequiredMixin
from braces.views import LoginRequiredMixin
from django.views.generic import TemplateView

# Create your views here.

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard.html"
    login_url = '/login/'
    redirect_field_name = 'redirect_to'