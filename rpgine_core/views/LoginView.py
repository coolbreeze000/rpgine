from django.shortcuts import redirect

from rpgine_core.forms.LoginForm import LoginForm

from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth import login, logout

class LoginView(View):
    def login(request):
        logout(request)

        form = LoginForm(request.POST or None)

        if request.POST and form.is_valid():
            user = form.login(request)

            if user is not None:
                login(request, user)
                redirect('dashboard')