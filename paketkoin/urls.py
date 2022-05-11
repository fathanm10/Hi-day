from django.urls import path
from . import views

app_name = 'paketkoin'

urlpatterns = [
    path('', views.index, name='index'),
    path('buat/', views.buat, name='buat'),
    path('transaksi/', views.transaksi, name='transaksi'),
    path('edit/<int:jumlah_koin>/<str:cmd>/', views.edit, name='edit')
]