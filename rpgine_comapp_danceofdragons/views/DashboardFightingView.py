from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/login/', redirect_field_name=None)
class DashboardFightingView(View):
    def get(self, request):
        return render(request, 'danceofdragons/fighting.html')