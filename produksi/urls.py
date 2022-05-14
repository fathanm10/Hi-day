from django.urls import path
from . import views

app_name = 'produksi'

urlpatterns = [
    path('list-produk', views.list_produk, name='list_produksi'),
]