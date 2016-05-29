from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import RedirectView
from django.contrib.auth import logout
from django.shortcuts import redirect

class LogoutView(LoginRequiredMixin, RedirectView):
    permanent = True
    query_string = False
    pattern_name = 'login'
    url = 'login'

    def get(self, request, *args, **kwargs):
        print("LOGOUT!")
        logout(request)
        return redirect('login')