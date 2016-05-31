from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
"""
from tabination.views import TabView
from django.utils.translation import ugettext as _
"""

# Create your views here.

class DashboardDiceRollerView(LoginRequiredMixin, TemplateView):
    template_name = "danceofdragons/dashboard_diceroller.html"
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

class DashboardDiceRollerSimpleView(LoginRequiredMixin, TemplateView):
    template_name = "danceofdragons/dashboard_diceroller.html"
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

class DashboardDiceRollerExtendedView(LoginRequiredMixin, TemplateView):
    template_name = "danceofdragons/dashboard_diceroller.html"
    login_url = '/login/'
    redirect_field_name = 'redirect_to'


class DashboardDiceRollerContestedView(LoginRequiredMixin, TemplateView):
    template_name = "danceofdragons/dashboard_diceroller.html"
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

"""
class DashboardDiceRollerBaseTab(LoginRequiredMixin, TabView):
    tab_group = 'main_navigation'
    tab_classes = ['main-navigation-tab']

    def get_context_data(self, **kwargs):
        context = super(DashboardDiceRollerBaseTab, self).get_context_data(**kwargs)
        context['spam'] = 'ham'
        return context

class DashboardDiceRollerSimpleTab(LoginRequiredMixin, DashboardDiceRollerBaseTab):
    _is_tab = True
    tab_id = 'roller_simple'
    tab_label = _('Simple Rolls')
    template_name = "danceofdragons/dashboard_diceroller.html"
"""