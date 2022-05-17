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
    path('transaksi/create', views.create_transaksi_beli_aset, name='create-transaksi-beli-aset'),

    path('create', views.create_aset_list, name='create-aset-list'),
    path('create/dekorasi', views.create_dekorasi, name='create-dekorasi'),
    path('create/bibit-tanaman', views.create_bibit_tanaman, name='create-bibit-tanaman'),
    path('create/kandang', views.create_kandang, name='create-kandang'),
    path('create/hewan', views.create_hewan, name='create-hewan'),
    path('create/alat-produksi', views.create_alat_produksi, name='create-alat-produksi'),
    path('create/petak-sawah', views.create_petak_sawah, name='create-petak-sawah'),
    
    path('update/dekorasi/<str:id>', views.update_dekorasi, name='update-dekorasi'),
    path('update/bibit-tanaman/<str:id>', views.update_bibit_tanaman, name='update-bibit-tanaman'),
    path('update/kandang/<str:id>', views.update_kandang, name='update-kandang'),
    path('update/hewan/<str:id>', views.update_hewan, name='update-hewan'),
    path('update/alat-produksi/<str:id>', views.update_alat_produksi, name='update-alat-produksi'),
    path('update/petak-sawah/<str:id>', views.update_petak_sawah, name='update-petak-sawah'),
]