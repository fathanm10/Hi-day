from django.shortcuts import redirect, render
from django.template.defaulttags import register
from hi_day.utils import get_query
from hi_day.auth import is_authenticated, get_role, get_session_data

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

def index(request):
    return redirect('/')

def histori_tanaman(request):
    data = get_session_data(request)
    daftarhistory = get_query(
        f"""
        SELECT * from HISTORI_TANAMAN NATURAL JOIN HISTORI_PRODUKSI
        """
    )
    print(daftarhistory)
    return render(request, 'prosesproduksi/histori_tanaman.html', {
        'title': "Histori Tanaman",
        'data':data,
        'daftarhistory':daftarhistory
    })