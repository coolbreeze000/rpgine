from django.shortcuts import redirect

from rpgine_core.views.LogoutView import logout
from rpgine_core.forms.LoginForm import LoginForm

from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout

class DashboardView(View):
    def get(self, request):
        return render(request, 'core/../templates/login.html')

    def login(request):
        logout(request)

        form = LoginForm(request.POST or None)

        if request.POST and form.is_valid():
            user = form.login(request)

            if user is not None:
                login(request, user)
                redirect('dashboard')