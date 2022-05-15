from django.urls import path
from . import views

app_name = 'prosesproduksi'

urlpatterns = [
    path('', views.index, name='index'),
    path('histori_tanaman', views.histori_tanaman, name='histori_tanaman'),
]