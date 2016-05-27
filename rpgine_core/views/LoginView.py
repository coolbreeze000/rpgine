from django.shortcuts import redirect

from rpgine_core.forms.LoginForm import LoginForm
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout

class LoginView(FormView):
    template_name = "login.html"
    form_class = LoginForm
    success_url = 'dashboard.html'

    def login(request):
        logout(request)

        form = LoginForm(request.POST or None)

        if request.POST and form.is_valid():
            user = form.login(request)

            if user is not None:
                login(request, user)
                redirect('dashboard')