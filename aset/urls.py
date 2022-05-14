from django.urls import path
from . import views

app_name = 'aset'

urlpatterns = [
    path('', views.list_tipe_aset, name='list-tipe-aset'),
    path('dekorasi', views.list_dekorasi, name='list-dekorasi'),
    path('bibit-tanaman', views.list_bibit_tanaman, name='list-bibit-tanaman'),
    path('kandang', views.list_kandang, name='list-kandang'),
    path('hewan', views.list_hewan, name='list-hewan'),
    path('alat-produksi', views.list_alat_produksi, name='list-alat-produksi'),
    path('petak-sawah', views.list_petak_sawah, name='list-petak-sawah'),

    path('koleksi', views.list_koleksi_aset, name='list-koleksi-aset'),
    path('koleksi/dekorasi', views.list_koleksi_dekorasi, name='list-koleksi-dekorasi'),
    path('koleksi/bibit-tanaman', views.list_koleksi_bibit_tanaman, name='list-koleksi-bibit-tanaman'),
    path('koleksi/kandang', views.list_koleksi_kandang, name='list-koleksi-kandang'),
    path('koleksi/hewan', views.list_koleksi_hewan, name='list-koleksi-hewan'),
    path('koleksi/alat-produksi', views.list_koleksi_alat_produksi, name='list-koleksi-alat_produksi'),
    path('koleksi/petak-sawah', views.list_koleksi_petak_sawah, name='list-koleksi-petak-sawah'),

    path('transaksi', views.list_transaksi_pembelian_aset, name='list-transaksi-pembelian-aset'),

]