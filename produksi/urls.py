from django.urls import path
from . import views

app_name = 'produksi'

urlpatterns = [
    path('list-produksi/', views.list_produksi, name='list_produksi'),
    path('detail-produksi/<pk>', views.detail_produksi, name='detail_produksi'),
]