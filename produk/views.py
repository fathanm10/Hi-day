from django.http import HttpResponse
from django.shortcuts import redirect, render
from hi_day.utils import get_query
from hi_day.auth import is_authenticated, get_role, get_session_data
from django.views.decorators.csrf import csrf_exempt


def list_produk(request):
    if not is_authenticated(request):
        return redirect("/auth/login")

    data = {}
    data['role'] = get_role(request.session['email'],
                            request.session['password'])
    data['user'] = get_session_data(request)

    product_data = []
    result = get_query(f'''
            SELECT P.nama, P.harga_jual, P.sifat_produk, 
            PH.ID_Produk AS ph_id, HP.ID_produk AS hp_id, PM.ID_produk AS pm_id
            FROM produk AS P
            FULL JOIN produk_hewan AS PH
            ON PH.ID_produk = P.ID
            FULL JOIN hasil_panen AS HP
            ON HP.ID_produk = P.ID
            FULL JOIN produk_makanan AS PM
            ON PM.ID_produk = P.ID;
        ''')

    for i in range(len(result)):
        jenis = ""
        if (result[i][3] is not None):
            jenis = "Produk Hewan"
        elif (result[i][4] is not None):
            jenis = "Hasil Panen"
        else:
            jenis = "Produk Makanan"

        product_data.append({
            'nama': result[i][0],
            'harga': result[i][1],
            'sifat': result[i][2],
            'jenis': jenis,
        })

    data['product'] = product_data

    return render(request, 'produk/list_produk.html', {'title': "List Produk", 'data': data})


@csrf_exempt
def add_product(request):
    next = request.GET.get("next")

    data = {}
    data['role'] = get_role(request.session['email'],
                            request.session['password'])
    data['user'] = get_session_data(request)

    if request.method != "POST":
        if not is_authenticated(request):
            return redirect("/auth/login")
        return render(request, 'produk/add_produk.html', {'title': "Tambah Produk", 'data': data})

    body = request.POST

    jenis = body['jenis']
    nama = body['nama']
    harga = body['harga']
    sifat = body['sifat']

    id = ""
    if (jenis == "panen"):
        current_id = get_query('''
            SELECT COUNT(*)
            FROM hasil_panen;
        ''')
        id = "HP" + str(current_id[0][0] + 1)

        get_query(f'''
            INSERT INTO produk VALUES
            ('{id}', '{nama}', {harga}, '{sifat}');

            INSERT INTO hasil_panen VALUES
            ('{id}');
        ''')
    elif (jenis == "hewan"):
        current_id = get_query('''
            SELECT COUNT(*)
            FROM produk_hewan;
        ''')
        id = "PH" + str(current_id[0][0] + 1)

        get_query(f'''
            INSERT INTO produk VALUES
            ('{id}', '{nama}', {harga}, '{sifat}');

            INSERT INTO produk_hewan VALUES
            ('{id}');
        ''')
    else:
        current_id = get_query('''
            SELECT COUNT(*)
            FROM produk_makanan;
        ''')
        id = "PM" + str(current_id[0][0] + 1)

        get_query(f'''
            INSERT INTO produk VALUES
            ('{id}', '{nama}', {harga}, '{sifat}');

            INSERT INTO produk_makanan VALUES
            ('{id}');
        ''')

    if next != None and next != "None":
        return redirect(next)
    else:
        return redirect("/produk/list-produk")
