from django.shortcuts import redirect, render
from django.template.defaulttags import register
from hi_day.utils import get_query
from hi_day.auth import is_authenticated, get_role, get_session_data

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

def index(request):
    if not is_authenticated(request):
        return redirect("/auth/login")
    data = get_session_data(request)
    print(data['role'])

    return render(request, 'lumbung/index.html', {'title': "Detail Lumbung", 'data':data})

def transaksi(request):
    data = get_session_data(request)
    if data['role'] == 'admin':
        daftartransaksi = get_query(
            f"""
            SELECT * from TRANSAKSI_UPGRADE_LUMBUNG
            """
        )
    elif data['role'] == 'user':
        daftartransaksi = get_query(
            f"""
            SELECT * from TRANSAKSI_UPGRADE_LUMBUNG
            WHERE email = '{request.session['email']}'
            """
        )
    print(daftartransaksi)
    return render(request, 'lumbung/transaksi.html', {
        'title': "Transaksi Upgrade Lumbung",
        'data':data,
        'daftartransaksi':daftartransaksi
    })