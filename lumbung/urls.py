from django.urls import path
from . import views

app_name = 'lumbung'

urlpatterns = [
    path('', views.index, name='isi_lumbung'),
]