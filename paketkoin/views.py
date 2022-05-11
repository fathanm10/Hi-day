from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
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
    
    paketkoin = get_query(
        f'''
        SELECT * FROM paket_koin;
        ''')
    print(paketkoin)

    return render(request, 'paketkoin/index.html', {
        'title': "Home",
        'paketkoin':paketkoin,
        'data':data,
    })

@csrf_exempt
def buat(request):
    data = get_session_data(request)
    if request.method != "POST":
        return render(request, 'paketkoin/buat.html', {
            'title': "Buat Paket Koin",
            'data':data
        })
    
    jumlah_koin = request.POST["jumlah_koin"]
    harga = request.POST["harga"]
    
    if jumlah_koin == "":
        messages.error(request, 'Input masih ada yang kosong')
        return redirect("/paketkoin/buat")

    try:
        jumlah_koin = int(jumlah_koin)
        harga = int(harga)
    except:
        messages.error(request, 'Input bukan desimal')
        return redirect("/paketkoin/buat")
    
    print("GET")
    result = get_query(
        f"""
        INSERT INTO paket_koin VALUES
        ('{jumlah_koin}','{harga}');
        """
    )

    return redirect("/paketkoin")

@csrf_exempt
def edit(request, jumlah_koin, cmd):
    data = get_session_data(request)
    if request.method != "POST":
        if cmd == 'delete':
            get_query(
                f"""
                DELETE FROM paket_koin
                WHERE jumlah_koin = '{jumlah_koin}'
                """
            )
            return redirect("/paketkoin")
        elif cmd == 'update':
            return render(request, 'paketkoin/ubah.html', {
                'title': "Edit Paket Koin",
                'data': data,
                'jumlah_koin': jumlah_koin
            })
    
    harga = request.POST["harga"]
    if harga == "":
        messages.error(request, 'Input masih ada yang kosong')
        return render(request, 'paketkoin/ubah.html', {
            'title': "Edit Paket Koin",
            'data': data,
            'jumlah_koin': jumlah_koin
        })
    
    try:
        harga = int(harga)
    except:
        messages.error(request, 'Input bukan desimal')
        return render(request, 'paketkoin/ubah.html', {
            'title': "Edit Paket Koin",
            'data': data,
            'jumlah_koin': jumlah_koin
        })


    result = get_query(
        f"""
        UPDATE paket_koin
        SET harga = '
        """
    )
    return redirect("/paketkoin")

@csrf_exempt
def ubah(request):
    data = get_session_data(request)
    if request.method != "POST":
        return render(request, 'paketkoin/ubah.html', {
            'title': "Buat Paket Koin",
            'data':data
        })
    
    jumlah_koin = request.POST["jumlah_koin"]
    harga = request.POST["harga"]
    
    if (jumlah_koin == "") or (harga == ""):
        messages.error(request, 'Input masih ada yang kosong')
        return redirect("/paketkoin/buat")

    try:
        jumlah_koin = int(jumlah_koin)
        harga = int(harga)
    except:
        messages.error(request, 'Input bukan desimal')
        return redirect("/paketkoin/buat")
    
    print("GET")
    result = get_query(
        f"""
        INSERT INTO paket_koin VALUES
        ('{jumlah_koin}','{harga}');
        """
    )

    return redirect("/paketkoin")

def transaksi(request):
    data = get_session_data(request)
    daftartransaksi = get_query(
        f"""
        SELECT * from TRANSAKSI_PEMBELIAN_KOIN
        """
    )
    print(daftartransaksi)
    return render(request, 'paketkoin/transaksi.html', {
        'title': "Transaksi Pembelian Koin",
        'data':data,
        'daftartransaksi':daftartransaksi
    })