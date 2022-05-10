from django.shortcuts import redirect
from django.urls import path
from . import views

app_name = 'login'

urlpatterns = [
    path('', views.index, name='login_index'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('register/admin', views.register_admin, name='register_admin'),
    path('register/user', views.register_user, name='register_user'),
    path('logout', views.logout, name='logout'),
]
