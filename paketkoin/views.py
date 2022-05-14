from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.template.defaulttags import register

from hi_day.utils import get_query
from hi_day.auth import is_authenticated, get_role, get_session_data

import datetime

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
        'title': "List Paket Koin",
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

    if (jumlah_beli == "") or (harga == ""):
        messages.error(request, "Data yang diisikan belum lengkap, silahkan lengkapi data terlebih dahulu")
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
        messages.error(request, "Data yang diisikan belum lengkap, silahkan lengkapi data terlebih dahulu")
        return redirect(f"/paketkoin/ubah/{jumlah_koin}/{cmd}")
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
    if data['role'] == 'admin':
        daftartransaksi = get_query(
            f"""
            SELECT * from TRANSAKSI_PEMBELIAN_KOIN
            """
        )
    elif data['role'] == 'user':
        daftartransaksi = get_query(
            f"""
            SELECT * from TRANSAKSI_PEMBELIAN_KOIN
            WHERE email = '{request.session['email']}'
            """
        )
    print(daftartransaksi)
    return render(request, 'paketkoin/transaksi.html', {
        'title': "Transaksi Pembelian Koin",
        'data':data,
        'daftartransaksi':daftartransaksi
    })

@csrf_exempt
def beli(request, jumlah_koin):
    data = get_session_data(request)
    if request.method != 'POST':
        paket_koin = get_query(
            f"""
                SELECT * FROM paket_koin
                WHERE jumlah_koin = '{jumlah_koin}'
            """
        )
        print(paket_koin)
        return render(request, 'paketkoin/beli.html', {
            'title': "Pembelian Paket Koin",
            'data':data,
            'paket':paket_koin[0]
        })
    
    paket = request.POST["paket"]
    harga = request.POST["harga"]
    jumlah_beli = request.POST["jumlah_beli"]
    cara_bayar = request.POST["cara_bayar"]

    if (jumlah_beli == "") or (cara_bayar == ""):
        messages.error(request, "Data yang diisikan belum lengkap, silahkan lengkapi data terlebih dahulu")
        return redirect(f"/paketkoin/beli/{jumlah_koin}")
        
    try:
        jumlah_beli = int(jumlah_beli)
    except:
        messages.error(request, 'Input bukan desimal')
        return redirect(f"/paketkoin/beli/{jumlah_koin}")
    
    result = get_query(
        f"""
            INSERT INTO TRANSAKSI_PEMBELIAN_KOIN VALUES
            ('{request.session['email']}', '{datetime.datetime.now()}', '{jumlah_beli}', '{cara_bayar}', '{paket}', 0)
        """
    )

    return redirect("/paketkoin")