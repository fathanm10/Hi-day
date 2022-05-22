from django.urls import path
from . import views

app_name = 'prosesproduksi'

urlpatterns = [
    path('', views.index, name='index'),
    path('histori_tanaman', views.histori_tanaman, name='histori_tanaman'),
    path('produksi-makanan', views.produksi_makanan, name='produksi_makanan'),
    path('histori_makanan', views.histori_makanan, name='histori_makanan'),
]