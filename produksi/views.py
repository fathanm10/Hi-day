from django.http import HttpResponse
from django.shortcuts import redirect, render
from hi_day.utils import get_query
from hi_day.auth import is_authenticated, get_role, get_session_data
from django.contrib import messages


def list_produksi(request):
    if not is_authenticated(request):
        return redirect("/auth/login")

    data = {}
    data['role'] = get_role(request.session['email'],
                            request.session['password'])
    data['user'] = get_session_data(request)

    production_data = []
    result = get_query(f'''
            SELECT PM.nama AS produk, A.nama AS alat, P.durasi, P.jumlah_hasil_unit,
            A.ID as AID, PM.ID AS PID
            FROM produksi AS P
            INNER JOIN aset AS A
            ON A.ID = P.ID_alat_produksi
            INNER JOIN produk AS PM
            ON PM.ID = P.ID_produk_makanan;
        ''')

    print(result[1])

    for i in range(len(result)):
        production_data.append({
            "id": result[i][5] + "-" + result[i][4],
            "nama": result[i][0],
            "alat": result[i][1],
            "durasi": str(result[i][2]),
            "jumlah": result[i][3],
        })

    data['product'] = production_data

    return render(request, 'produksi/list_produksi.html', {'title': "List Produksi", 'data': data})


def detail_produksi(request, pk):
    if not is_authenticated(request):
        return redirect("/auth/login")

    data = {}
    data['role'] = get_role(request.session['email'],
                            request.session['password'])
    data['user'] = get_session_data(request)

    produk_makanan = pk.split("-")[0]
    alat_produksi = pk.split("-")[1]

    result = get_query(f'''
            SELECT PM.nama AS produk, A.nama AS alat, P.durasi, P.jumlah_hasil_unit
            FROM produksi AS P
            INNER JOIN aset AS A
            ON A.ID = P.ID_alat_produksi
            INNER JOIN produk AS PM
            ON PM.ID = P.ID_produk_makanan
            WHERE P.ID_produk_makanan='{produk_makanan}' AND P.ID_alat_produksi='{alat_produksi}';
        ''')

    component = get_query(f'''
        SELECT PM.nama, PPM.jumlah
        FROM produk_dibutuhkan_oleh_produk_makanan AS PPM
        INNER JOIN produk AS PM
        ON PM.ID = PPM.ID_produk_makanan
        WHERE ID_produk_makanan='{produk_makanan}';
    ''')
    print(result)
    print(component)

    bahan = []
    for i in range(len(component)):
        bahan.append({
            "nama":component[i][0],
            "jumlah":component[i][1],
        })

    production_data = {
        "nama": result[0][0],
        "alat": result[0][1],
        "durasi": str(result[0][2]),
        "jumlah": result[0][3],
        "bahan":bahan,
    }

    data['production'] = production_data

    return render(request, 'produksi/detail_produksi.html', {'title': "Detail Produksi", 'data': data})
