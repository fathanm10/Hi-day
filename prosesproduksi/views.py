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
