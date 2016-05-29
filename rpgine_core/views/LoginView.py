from rpgine_core.forms.LoginForm import LoginForm
from django.views.generic.edit import FormView
from django.contrib.auth import login
from django.shortcuts import redirect
from braces.views import AnonymousRequiredMixin

class LoginView(AnonymousRequiredMixin, FormView):
    template_name = "login.html"
    form_class = LoginForm
    success_url = '/dance-of-dragons/dashboard/'

    def get_authenticated_redirect_url(self):
        return self.success_url

    def form_valid(self, form):
        print("Invalid Login Credentials from User: " + form.get_user().get_username())
        login(self.request, form.get_user())

        if form.get_user().is_authenticated():
            print("Successful login to RPGine from User: " + form.get_user().get_username())

        return super(LoginView, self).form_valid(form)

    def form_invalid(self, form):
        print("Invalid Login Credentials from User")

        return super(LoginView, self).form_valid(form)