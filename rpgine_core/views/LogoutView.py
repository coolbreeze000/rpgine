from django.shortcuts import redirect

from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth import logout

class LogoutView(View):
    def logout(request):
        logout(request)
        redirect('login')