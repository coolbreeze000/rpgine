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
        regex=r'^dance-of-dragons/',
        view=danceofdragons_views_dashboard.as_view(),
        name="dashboard"
    ),
    url(
        regex=r'^dance-of-dragons/dashboard/',
        view=danceofdragons_views_dashboard.as_view(),
        name="dashboard"
    ),
    url(
        regex=r'^dance-of-dragons/contested-rolls/',
        view=danceofdragons_views_dashboarddiceroller.as_view(),
        name="simple-rolls"
    ),
    url(
        regex=r'^dance-of-dragons/contested-rolls/',
        view=danceofdragons_views_dashboarddiceroller.as_view(),
        name="extended-rolls"
    ),
    url(
        regex=r'^dance-of-dragons/contested-rolls/',
        view=danceofdragons_views_dashboarddiceroller.as_view(),
        name="contested-rolls"
    ),
    url(
        regex=r'^admin/',
        view=include(admin.site.urls),
        name="admin"
    ),
]

"""
    url(
        regex=r'^login/',
        view=rpginecore_views_login.as_view(),
        name="admin"
    ),
    url(
        regex=r'^logout/',
        view=rpginecore_views_logout.as_view(),
        name="admin"
    ),


    url(
        regex=r'^login/',
        view=include(auth_views.login, {'template_name': 'login.html'}),
        name="admin"
    ),
    url(
        regex=r'^logout/',
        view=include(auth_views.login, {'template_name': 'logout.html'}),
        name="admin"
    ),
    url(
        regex=r'^$',
        view=core_views_dashboard.as_view(),
        name="dashboard"
    ),
    url(
        regex=r'^dashboard/',
        view=core_views_dashboard.as_view(),
        name="dashboard"
    ),
"""