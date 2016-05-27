from django.shortcuts import render
from django.views.generic import TemplateView
#from django.contrib.auth.mixins import LoginRequiredMixin
#from rpgine_core.mixins.LoginRequiredMixin import LoginRequiredMixin
from braces.views import LoginRequiredMixin

# Create your views here.

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "danceofdragons/diceroller.html"
    login_url = '/login/'
    redirect_field_name = 'redirect_to'