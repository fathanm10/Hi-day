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
    if not is_authenticated(request):
        return redirect("/auth/login")

    data = {}
    data['role'] = get_role(request.session['email'],
                            request.session['password'])

    user_data = {}
    data['user'] = user_data

    lumbung = {}
    if (data['role'] == 'admin'):
        user_data = get_session_data(request)

        hewan = get_query(f'''
            SELECT L.email, P.ID, P.nama, P.harga_jual, P.sifat_produk, LP.jumlah
            FROM lumbung AS L
            INNER JOIN lumbung_memiliki_produk AS LP
            ON LP.ID_lumbung = L.email
            INNER JOIN produk AS P
            ON P.ID = LP.ID_produk
            INNER JOIN produk_hewan AS PH
            ON PH.ID_produk = P.ID;
        ''')
        makanan = get_query(f'''
            SELECT L.email, P.ID, P.nama, P.harga_jual, P.sifat_produk, LP.jumlah
            FROM lumbung AS L
            INNER JOIN lumbung_memiliki_produk AS LP
            ON LP.ID_lumbung = L.email
            INNER JOIN produk AS P
            ON P.ID = LP.ID_produk
            INNER JOIN produk_makanan AS PM
            ON PM.ID_produk = P.ID;
        ''')
        panen = get_query(f'''
            SELECT L.email, P.ID, P.nama, P.harga_jual, P.sifat_produk, LP.jumlah
            FROM lumbung AS L
            INNER JOIN lumbung_memiliki_produk AS LP
            ON LP.ID_lumbung = L.email
            INNER JOIN produk AS P
            ON P.ID = LP.ID_produk
            INNER JOIN hasil_panen AS HP
            ON HP.ID_produk = P.ID;
        ''')

        hasil_panen = []
        produk_hewan = []
        produk_makanan = []
        for i in range(len(panen)):
            hasil_panen.append({
                "email": panen[i][0],
                "id": panen[i][1],
                "nama": panen[i][2],
                "harga": panen[i][3],
                "sifat": panen[i][4],
                "jumlah": panen[i][5],
            })

        for i in range(len(hewan)):
            produk_hewan.append({
                "email": hewan[i][0],
                "id": hewan[i][1],
                "nama": hewan[i][2],
                "harga": hewan[i][3],
                "sifat": hewan[i][4],
                "jumlah": hewan[i][5],
            })
        for i in range(len(makanan)):
            produk_makanan.append({
                "email": makanan[i][0],
                "id": makanan[i][1],
                "nama": makanan[i][2],
                "harga": makanan[i][3],
                "sifat": makanan[i][4],
                "jumlah": makanan[i][5],
            })

        lumbung['produk'] = {
            "hasil_panen": hasil_panen,
            "produk_hewan": produk_hewan,
            "produk_makanan": produk_makanan,
        }
    elif (data['role'] == 'user'):
        email = request.session['email']
        result_user = get_query(f'''
            SELECT * FROM pengguna
            WHERE email='{email}';
        ''')
        user_data['email'] = result_user[0][0]
        user_data['farm'] = result_user[0][2]
        user_data['xp'] = result_user[0][3]
        user_data['koin'] = result_user[0][4]
        user_data['level'] = result_user[0][5]

        data_lumbung = get_query(f'''
            SELECT email, level, kapasitas_max, total
            FROM lumbung
            WHERE email='{email}';
        ''')

        hewan = get_query(f'''
            SELECT P.ID, P.nama, P.harga_jual, P.sifat_produk, LP.jumlah
            FROM lumbung AS L
            INNER JOIN lumbung_memiliki_produk AS LP
            ON LP.ID_lumbung = L.email
            INNER JOIN produk AS P
            ON P.ID = LP.ID_produk
            INNER JOIN produk_hewan AS PH
            ON PH.ID_produk = P.ID
            WHERE L.email='{email}';
        ''')
        makanan = get_query(f'''
            SELECT P.ID, P.nama, P.harga_jual, P.sifat_produk, LP.jumlah
            FROM lumbung AS L
            INNER JOIN lumbung_memiliki_produk AS LP
            ON LP.ID_lumbung = L.email
            INNER JOIN produk AS P
            ON P.ID = LP.ID_produk
            INNER JOIN produk_makanan AS PM
            ON PM.ID_produk = P.ID
            WHERE L.email='{email}';
        ''')
        panen = get_query(f'''
            SELECT P.ID, P.nama, P.harga_jual, P.sifat_produk, LP.jumlah
            FROM lumbung AS L
            INNER JOIN lumbung_memiliki_produk AS LP
            ON LP.ID_lumbung = L.email
            INNER JOIN produk AS P
            ON P.ID = LP.ID_produk
            INNER JOIN hasil_panen AS HP
            ON HP.ID_produk = P.ID
            WHERE L.email='{email}';
        ''')

        hasil_panen = []
        produk_hewan = []
        produk_makanan = []
        for i in range(len(panen)):
            hasil_panen.append({
                "id": panen[i][0],
                "nama": panen[i][1],
                "harga": panen[i][2],
                "sifat": panen[i][3],
                "jumlah": panen[i][4],
            })

        for i in range(len(hewan)):
            produk_hewan.append({
                "id": hewan[i][0],
                "nama": hewan[i][1],
                "harga": hewan[i][2],
                "sifat": hewan[i][3],
                "jumlah": hewan[i][4],
            })
        for i in range(len(makanan)):
            produk_makanan.append({
                "id": makanan[i][0],
                "nama": makanan[i][1],
                "harga": makanan[i][2],
                "sifat": makanan[i][3],
                "jumlah": makanan[i][4],
            })

        lumbung['produk'] = {
            "hasil_panen": hasil_panen,
            "produk_hewan": produk_hewan,
            "produk_makanan": produk_makanan,
        }

        lumbung['email'] = data_lumbung[0][0]
        lumbung['level'] = data_lumbung[0][1]
        lumbung['capacity_max'] = data_lumbung[0][2]
        lumbung['total'] = data_lumbung[0][3]
        lumbung['capacity'] = lumbung['capacity_max']//lumbung['total']

    data['lumbung'] = lumbung
    data['user'] = user_data

    return render(request, 'lumbung/index.html', {'title': "Detail Lumbung", 'data': data})


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
        'data': data,
        'daftartransaksi': daftartransaksi
    })

@csrf_exempt
def upgrade(request):
    data = get_session_data(request)
    user_data = {}
    if data['role'] == 'user':
        result = get_query(f'''
            SELECT * FROM lumbung
            WHERE email='{request.session['email']}';
        ''')
        print(result[0])
        user_data['email'] = result[0][0]
        user_data['level'] = result[0][1]
        user_data['new_level'] = int(result[0][1])+1
        user_data['cap'] = result[0][2]
        user_data['new_cap'] = int(result[0][2])+50
        user_data['total'] = result[0][3]
    data['user'] = user_data

    if request.method != "POST":
        return render(request, 'lumbung/upgrade.html', {
            'title': "Upgrade Lumbung",
            'data': data,
        })

    level = user_data["new_level"]
    cap = user_data["new_cap"]
    biaya = request.POST["biaya"]
    time = datetime.now()

    result_lumbung = get_query(
        f"""
        UPDATE LUMBUNG
        SET level = {level}, kapasitas_max = {cap}
        WHERE email = '{user_data['email']}'
        """
    )

    result_transaksi = get_query(
        f"""
        INSERT INTO TRANSAKSI_UPGRADE_LUMBUNG VALUES
        ('{user_data['email']}','{time}')
        """
    )

    return redirect("/lumbung/upgrade")