from django.shortcuts import render
from django.views.generic import View
#from django.contrib.auth.mixins import LoginRequiredMixin
#from rpgine_core.mixins.LoginRequiredMixin import LoginRequiredMixin
from braces.views import LoginRequiredMixin

# Create your views here.

class DashboardView(LoginRequiredMixin, View):
    template_name = "login.html"
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        return render(request, 'dashboard.html')