from django.urls import path
from . import views

app_name = 'prosesproduksi'

urlpatterns = [
    path('', views.index, name='index'),
    path('produksi_tanaman', views.produksi_tanaman, name='produksi_tanaman'),
    path('histori_tanaman', views.histori_tanaman, name='histori_tanaman'),
    path('histori_makanan', views.histori_makanan, name='histori_makanan'),
]