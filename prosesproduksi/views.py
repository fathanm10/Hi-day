from django.contrib import messages
from django.shortcuts import redirect, render
from django.template.defaulttags import register
from django.views.decorators.csrf import csrf_exempt

from hi_day.utils import get_query
from hi_day.auth import is_authenticated, get_role, get_session_data

from datetime import datetime

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


def index(request):
    return redirect('/')

@csrf_exempt
def produksi_tanaman(request):
    data = get_session_data(request)
    user_data = {}
    if request.method != 'POST':
        result_user = get_query(f'''
            SELECT * FROM pengguna
            WHERE email='{data['email']}';
        ''')
        user_data['email'] = result_user[0][0]
        user_data['farm'] = result_user[0][2]
        user_data['xp'] = result_user[0][3]
        user_data['koin'] = result_user[0][4]
        user_data['level'] = result_user[0][5]
        data['user'] = user_data

        result_bibit = get_query(f'''
            SELECT KAMA.id_koleksi_aset, KAMA.id_aset, A.nama, KAMA.jumlah
            from KOLEKSI_ASET_MEMILIKI_ASET KAMA
            INNER JOIN ASET A
            ON (KAMA.id_aset) = (A.id)
            INNER JOIN BIBIT_TANAMAN BT
            ON (A.id) = (BT.id_aset)
            WHERE KAMA.id_koleksi_aset = '{data['email']}'
        ''')

        print(result_bibit)
        bibits = result_bibit

        return render(request, 'prosesproduksi/produksi_tanaman.html', {
            'title':'Produksi Tanaman',
            'data':data,
            'bibits':bibits
        })

    bibit = request.POST['bibit']
    jumlah_stored = request.POST['jumlah_stored']
    jumlah = request.POST['jumlah']
    xp = request.POST['xp']
    time = datetime.now()
    if (jumlah == ""):
        messages.error(request, "Data yang diisikan belum lengkap, silahkan lengkapi data terlebih dahulu")
        return redirect("/prosesproduksi/produksi_tanaman")

    try:
        jumlah = int(jumlah)
    except:
        messages.error(request, 'Input bukan desimal')
        return redirect("/prosesproduksi/produksi_tanaman")

    print(jumlah,jumlah_stored)
    if int(jumlah) > int(jumlah_stored):
        messages.error(request, 'Anda tidak memiliki bibit yang cukup, silahkan membeli bibit terlebih dahulu')
        return redirect("/prosesproduksi/produksi_tanaman")

    result = get_query(f'''
        INSERT INTO HISTORI_PRODUKSI VALUES
        ('{data['email']}','{time}','{time}','{jumlah}','{xp}')
    ''')
    print(result)

    result = get_query(f'''
        INSERT INTO HISTORI_TANAMAN VALUES
        ('{data['email']}','{time}','{bibit['id_aset']}')
    ''')
    return redirect("/prosesproduksi/histori_tanaman")



def histori_tanaman(request):
    data = get_session_data(request)
    if data['role'] == 'admin':
        daftarhistory = get_query(
            f"""
            SELECT HT.email, HT.waktu_awal, HP.waktu_selesai, HP.jumlah, HP.xp, A.nama 
            from HISTORI_TANAMAN HT
            INNER JOIN HISTORI_PRODUKSI HP
            ON (HT.email, HT.waktu_awal) = (HP.email, HP.waktu_awal)
            INNER JOIN ASET A
            ON HT.id_bibit_tanaman = A.id
            """
        )
    elif data['role'] == 'user':
        daftarhistory = get_query(
            f"""
            SELECT HT.email, HT.waktu_awal, HP.waktu_selesai, HP.jumlah, HP.xp, A.nama 
            from HISTORI_TANAMAN HT
            INNER JOIN HISTORI_PRODUKSI HP
            ON (HT.email, HT.waktu_awal) = (HP.email, HP.waktu_awal)
            INNER JOIN ASET A
            ON HT.id_bibit_tanaman = A.id
            WHERE HT.email = '{request.session['email']}'
            """
        )
    print(daftarhistory)
    return render(request, 'prosesproduksi/histori_tanaman.html', {
        'title': "Histori Tanaman",
        'data': data,
        'daftarhistory': daftarhistory
    })


def histori_makanan(request):
    if not is_authenticated(request):
        return redirect("/auth/login")

    data = get_session_data(request)
    if data['role'] == 'admin':
        daftarhistory = get_query(
            f"""
            SELECT HP.email, HP.waktu_awal, HP.waktu_selesai, 
            HP.jumlah, HP.xp, P.nama AS makanan, A.nama AS alat
            FROM histori_produksi_makanan AS PM
            INNER JOIN histori_produksi HP
            ON (HP.email, HP.waktu_awal) =(PM.email, PM.waktu_awal)
            INNER JOIN produksi AS PR
            ON (PR.ID_alat_produksi, PR.ID_produk_makanan) = (PM.ID_alat_produksi, PM.ID_produk_makanan)
            INNER JOIN produk AS P
            ON P.ID = PR.ID_produk_makanan
            INNER JOIN aset AS A
            ON A.ID = PR.ID_alat_produksi;
            """
        )
    elif data['role'] == 'user':
        daftarhistory = get_query(
            f"""
            SELECT HP.email, HP.waktu_awal, HP.waktu_selesai, 
            HP.jumlah, HP.xp, P.nama AS makanan, A.nama AS alat
            FROM histori_produksi_makanan AS PM
            INNER JOIN histori_produksi HP
            ON (HP.email, HP.waktu_awal) =(PM.email, PM.waktu_awal)
            INNER JOIN produksi AS PR
            ON (PR.ID_alat_produksi, PR.ID_produk_makanan) = (PM.ID_alat_produksi, PM.ID_produk_makanan)
            INNER JOIN produk AS P
            ON P.ID = PR.ID_produk_makanan
            INNER JOIN aset AS A
            ON A.ID = PR.ID_alat_produksi
            WHERE HP.email = '{request.session['email']}'
            """
        )
    # print(daftarhistory)

    return render(request, 'prosesproduksi/histori_makanan.html', {
        'title': "Histori Makanan",
        'data': data,
        'daftarhistory': daftarhistory
    })
