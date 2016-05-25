from django.shortcuts import render
from django.views.generic import View

# Create your views here.

class DashboardEconomyView(View):
    def get(self, request):
        return render(request, 'danceofdragons/economy.html')