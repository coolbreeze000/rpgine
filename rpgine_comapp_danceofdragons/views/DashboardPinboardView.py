from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

# Create your views here.

class DashboardPinboardView(LoginRequiredMixin, TemplateView):
    template_name = "danceofdragons/dashboard_pinboard.html"
    login_url = '/login/'
    redirect_field_name = 'redirect_to'