from django.urls import path
from . import views

app_name = 'produk'

urlpatterns = [
    path('list-produk', views.list_produk, name='list_produk'),
]