from django.shortcuts import redirect

from rpgine_core.views.LogoutView import logout
from rpgine_core.forms.LoginForm import LoginForm

from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout

class DashboardView(View):
    def get(self, request):
        return render(request, 'core/../templates/logout.html')

    def logout(request):
        logout(request)
        redirect('login')