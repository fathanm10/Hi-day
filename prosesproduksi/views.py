from django.shortcuts import redirect, render
from django.template.defaulttags import register
from hi_day.utils import get_query
from hi_day.auth import is_authenticated, get_role, get_session_data
from django.contrib import messages
from datetime import datetime


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
            SELECT * from HISTORI_TANAMAN NATURAL JOIN HISTORI_PRODUKSI
            """
        )
    elif data['role'] == 'user':
        daftarhistory = get_query(
            f"""
            SELECT * from HISTORI_TANAMAN NATURAL JOIN HISTORI_PRODUKSI
            WHERE email = '{request.session['email']}'
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


def produksi_makanan(request):
    data = {}
    data['role'] = get_role(request.session['email'],
                            request.session['password'])
    data['user'] = get_session_data(request)

    if request.method != "POST":
        if not is_authenticated(request):
            return redirect("/auth/login")
        makanan = []
        data_makanan = get_query('''
            SELECT P.nama, P.ID
            FROM produk AS P
            INNER JOIN produk_makanan AS PM
            ON PM.ID_Produk = P.ID;
        ''')
        for i in range(len(data_makanan)):
            makanan.append({
                "nama": data_makanan[i][0],
                "id": data_makanan[i][1],
            })
        data['makanan'] = makanan

        return render(request, 'prosesproduksi/produksi_makanan.html', {'title': "Buat Produksi Makanan", 'data': data})

    body = request.POST
    makanan = body['makanan']
    jumlah = int(body['jumlah'])
    xp = body['xp']

    data_produk = get_query(f'''
        SELECT id_produk, jumlah, id_produk_makanan
        FROM produk_dibutuhkan_oleh_produk_makanan
        WHERE id_produk_makanan='{makanan}';
    ''')
    # print(data_produk)

    data_lumbung = []
    for i in range(len(data_produk)):
        lumbung = get_query(f'''
        SELECT jumlah
        FROM lumbung_memiliki_produk
        WHERE id_lumbung='{data["user"]['email']}' AND id_produk='{data_produk[i][0]}';
    ''')
        print(int(data_produk[i][1])*jumlah)
        if (len(lumbung) == 0 or (int(data_produk[i][1])*jumlah) > lumbung[0][0]):
            data_lumbung.append(False)
        else:
            data_lumbung.append(True)
    # print(data_lumbung)

    data_alat = get_query(f'''
        SELECT A.ID_aset
        FROM produksi P
        INNER JOIN koleksi_aset_memiliki_aset A
        ON A.ID_aset = P.id_alat_produksi
        WHERE A.id_koleksi_aset='{data["user"]['email']}' AND P.id_produk_makanan='{makanan}';
    ''')
    # print(data_alat)

    if ((False in data_lumbung) or len(data_alat) == 0):
        messages.error(request, 'Produksi tidak bisa dilakukan')
        return redirect('/prosesproduksi/produksi-makanan')

    now = datetime.now()
    nowtime = now.strftime("%Y-%m-%d %H:%M:%S")

    get_query(f'''
        INSERT INTO histori_produksi VALUES
        ('{data['user']['email']}', '{nowtime}', '{nowtime}', '{jumlah}', '{xp}');

        INSERT INTO histori_produksi_makanan VALUES
        ('{data['user']['email']}', '{nowtime}', '{data_alat[0][0]}', '{data_produk[0][2]}');
    ''')

    messages.success(request, 'Produksi berhasil dilakukan')
    return redirect('/prosesproduksi/histori_makanan')
