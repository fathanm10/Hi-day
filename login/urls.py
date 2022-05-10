from django.shortcuts import redirect
from django.views.generic.base import RedirectView
from django.urls import path
from . import views

app_name = 'login'

urlpatterns = [
    path('', views.index, name='login_index'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
]
