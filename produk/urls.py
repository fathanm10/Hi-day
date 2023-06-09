from django.urls import path
from . import views

app_name = 'produk'

urlpatterns = [
    path('list-produk', views.list_produk, name='list_produk'),
    path('buat-produk', views.add_product, name='add_produk'),
    path('update-produk/<pk>', views.update_product, name='update_produk'),
    path('delete-produk/<pk>', views.delete_product, name='delete_produk'),
]