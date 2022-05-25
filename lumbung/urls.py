from django.urls import path
from . import views

app_name = 'lumbung'

urlpatterns = [
    path('', views.index, name='isi_lumbung'),
    path('transaksi', views.transaksi, name='transaksi'),
    path('upgrade', views.upgrade, name='upgrade'),
]