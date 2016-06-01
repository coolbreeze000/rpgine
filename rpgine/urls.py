"""rpgine URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from rpgine_core.views.LoginView import LoginView as rpginecore_views_login
from rpgine_core.views.LogoutView import LogoutView as rpginecore_views_logout
from rpgine_comapp_danceofdragons.views.DashboardView import DashboardView as danceofdragons_views_dashboard
from rpgine_comapp_danceofdragons.views.DashboardDiceRollerView import DashboardDiceRollerView as danceofdragons_views_dashboarddiceroller
from rpgine_comapp_danceofdragons.views.DashboardDiceRollerView import DashboardDiceRollerSimpleView as danceofdragons_views_dashboarddicerollersimple
from rpgine_comapp_danceofdragons.views.DashboardDiceRollerView import DashboardDiceRollerExtendedView as danceofdragons_views_dashboarddicerollerextended
from rpgine_comapp_danceofdragons.views.DashboardDiceRollerView import DashboardDiceRollerContestedView as danceofdragons_views_dashboarddicerollercontested
from rpgine_comapp_danceofdragons.views.DashboardFightingView import DashboardFightingView as danceofdragons_views_dashboardfighting
from rpgine_comapp_danceofdragons.views.DashboardEconomyView import DashboardEconomyView as danceofdragons_views_dashboardeconomy
from rpgine_comapp_danceofdragons.views.DashboardEspionageView import DashboardEspionageView as danceofdragons_views_dashboardespionage
from rpgine_comapp_danceofdragons.views.DashboardRelationshipsView import DashboardRelationshipsView as danceofdragons_views_dashboardrelationships
from rpgine_comapp_danceofdragons.views.DashboardPinboardView import DashboardPinboardView as danceofdragons_views_dashboardpinboard
from rpgine_comapp_danceofdragons.views.DashboardMapsView import DashboardMapsView as danceofdragons_views_dashboardmaps

urlpatterns = [
    url(
        regex=r'^$',
        view=danceofdragons_views_dashboard.as_view(),
        name="dashboard"
    ),
    url(
        regex=r'^login/',
        view=rpginecore_views_login.as_view(),
        name="login"
    ),
    url(
        regex=r'^logout/',
        view=rpginecore_views_logout.as_view(),
        name="logout"
    ),
    url(
        regex=r'^dance-of-dragons/$',
        view=danceofdragons_views_dashboard.as_view(),
        name="dashboard"
    ),
    url(
        regex=r'^dance-of-dragons/dashboard/$',
        view=danceofdragons_views_dashboard.as_view(),
        name="dashboard"
    ),
    url(
        regex=r'^dance-of-dragons/dice-roller/$',
        view=danceofdragons_views_dashboarddiceroller.as_view(),
        name="simple-rolls"
    ),
    url(
        regex=r'^dance-of-dragons/dice-roller/simple-rolls/$',
        view=danceofdragons_views_dashboarddicerollersimple.as_view(),
        name="simple-rolls"
    ),
    url(
        regex=r'^dance-of-dragons/dice-roller/extended-rolls/$',
        view=danceofdragons_views_dashboarddicerollerextended.as_view(),
        name="extended-rolls"
    ),
    url(
        regex=r'^dance-of-dragons/dice-roller/contested-rolls/$',
        view=danceofdragons_views_dashboarddicerollercontested.as_view(),
        name="contested-rolls"
    ),
    url(
        regex=r'^dance-of-dragons/fighting/$',
        view=danceofdragons_views_dashboardfighting.as_view(),
        name="fighting"
    ),
    url(
        regex=r'^dance-of-dragons/economy/$',
        view=danceofdragons_views_dashboardeconomy.as_view(),
        name="economy"
    ),
    url(
        regex=r'^dance-of-dragons/espionage/$',
        view=danceofdragons_views_dashboardespionage.as_view(),
        name="espionage"
    ),
    url(
        regex=r'^dance-of-dragons/relationships/$',
        view=danceofdragons_views_dashboardrelationships.as_view(),
        name="relationships"
    ),
    url(
        regex=r'^dance-of-dragons/fighting/$',
        view=danceofdragons_views_dashboardfighting.as_view(),
        name="character-fighting"
    ),
    url(
        regex=r'^dance-of-dragons/fighting/character-fights$',
        view=danceofdragons_views_dashboardfighting.as_view(),
        name="character-fighting"
    ),
    url(
        regex=r'^dance-of-dragons/fighting/tabletop-fights$',
        view=danceofdragons_views_dashboardfighting.as_view(),
        name="tabletop-fighting"
    ),
    url(
        regex=r'^dance-of-dragons/fighting/siege-fights$',
        view=danceofdragons_views_dashboardfighting.as_view(),
        name="siege-fighting"
    ),
    url(
        regex=r'^dance-of-dragons/pinboard/$',
        view=danceofdragons_views_dashboardpinboard.as_view(),
        name="pinboard"
    ),
    url(
        regex=r'^dance-of-dragons/maps/$',
        view=danceofdragons_views_dashboardmaps.as_view(),
        name="maps"
    ),
    url(
        regex=r'^admin/',
        view=include(admin.site.urls),
        name="admin"
    ),
]