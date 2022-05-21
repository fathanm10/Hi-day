from django.http import HttpResponse
from django.shortcuts import redirect, render
from hi_day.utils import get_query
from hi_day.auth import is_authenticated, get_role, get_session_data
from django.contrib import messages


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
            PH.ID_Produk AS ph_id, HP.ID_produk AS hp_id, PM.ID_produk AS pm_id, P.ID
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
            "id": result[i][6],
        })

    data['product'] = product_data

    return render(request, 'produk/list_produk.html', {'title': "List Produk", 'data': data})


def add_product(request):
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
            SELECT MAX(id_produk)
            FROM hasil_panen;
        ''')
        id = "HP" + str(int(current_id[0][0][2:]) + 1)

        get_query(f'''
            INSERT INTO produk VALUES
            ('{id}', '{nama}', {harga}, '{sifat}');

            INSERT INTO hasil_panen VALUES
            ('{id}');
        ''')
    elif (jenis == "hewan"):
        current_id = get_query('''
            SELECT MAX(id_produk)
            FROM produk_hewan;
        ''')
        id = "PH" + str(int(current_id[0][0][2:]) + 1)

        get_query(f'''
            INSERT INTO produk VALUES
            ('{id}', '{nama}', {harga}, '{sifat}');

            INSERT INTO produk_hewan VALUES
            ('{id}');
        ''')
    else:
        current_id = get_query('''
            SELECT MAX(id_produk)
            FROM produk_makanan;
        ''')
        id = "PM" + str(int(current_id[0][0][2:]) + 1)

        get_query(f'''
            INSERT INTO produk VALUES
            ('{id}', '{nama}', {harga}, '{sifat}');

            INSERT INTO produk_makanan VALUES
            ('{id}');
        ''')

    # Tidak perlu cek duplikat key, jadi langsung sukses
    messages.success(request, 'Produk berhasil ditambah')
    return redirect("/produk/list-produk")


def update_product(request, pk):
    data = {}
    data['role'] = get_role(request.session['email'],
                            request.session['password'])
    data['user'] = get_session_data(request)

    product_data = get_query(f'''
        SELECT *
        FROM produk
        WHERE ID='{pk}';
    ''')

    data['product'] = {
        'id': product_data[0][0],
        'nama': product_data[0][1],
        'harga': product_data[0][2],
        'sifat': product_data[0][3],
    }

    if request.method != "POST":
        if not is_authenticated(request):
            return redirect("/auth/login")
        return render(request, 'produk/update_produk.html', {'title': "Update " + data['product']['nama'], 'data': data})

    body = request.POST

    harga = body['harga']
    sifat = body['sifat']

    get_query(f'''
        UPDATE produk
        SET harga_jual='{harga}', sifat_produk='{sifat}'
        WHERE ID='{data['product']['id']}';
    ''')

    messages.success(request, 'Produk berhasil diupdate')
    return redirect("/produk/list-produk")


def delete_product(request, pk):
    data = {}
    data['role'] = get_role(request.session['email'],
                            request.session['password'])
    data['user'] = get_session_data(request)

    if not is_authenticated(request):
        return redirect("/auth/login")

    if data['role'] != 'admin':
        return redirect("/produk/list-produk")

    product_data = 0

    produk_pesanan = get_query(f'''
        SELECT P.ID
        FROM produk P
        INNER JOIN detail_pesanan DP
        ON DP.ID_produk = P.ID
        WHERE P.ID='{pk}';
    ''')
    # print(produk_pesanan)

    produk_lumbung = get_query(f'''
        SELECT P.ID
        FROM produk P
        INNER JOIN lumbung_memiliki_produk LP
        ON LP.ID_produk = P.ID
        WHERE P.ID='{pk}';
    ''')
    # print(produk_lumbung)

    produk_makanan = get_query(f'''
        SELECT P.ID
        FROM produk P
        INNER JOIN produk_dibutuhkan_oleh_produk_makanan PPM
        ON PPM.ID_produk = P.ID
        WHERE P.ID='{pk}';
    ''')
    # print(produk_makanan)

    produk_produksi = get_query(f'''
        SELECT P.ID
        FROM produk P
        INNER JOIN produksi AS PR
        ON PR.ID_produk_makanan = P.ID
        WHERE P.ID='{pk}';
    ''')
    # print(produk_produksi)

    produk_hewan = get_query(f'''
        SELECT P.ID
        FROM produk P
        INNER JOIN hewan_menghasilkan_produk_hewan AS H
        ON H.ID_Produk_Hewan = P.ID
        WHERE P.ID='{pk}';
    ''')
    # print(produk_hewan)

    produk_panen = get_query(f'''
        SELECT P.ID
        FROM produk P
        INNER JOIN bibit_tanaman_menghasilkan_hasil_panen AS BT
        ON BT.ID_Hasil_Panen = P.ID
        WHERE P.ID='{pk}';
    ''')
    # print(produk_panen)

    product_data += len(produk_pesanan) + \
        len(produk_lumbung) + len(produk_makanan) + \
        len(produk_produksi) + len(produk_hewan) + len(produk_panen)

    # print(product_data)

    if (product_data != 0):
        messages.error(request, 'Produk tidak bisa dihapus')
    else:
        get_query(f'''
            DELETE FROM produk CASCADE
            WHERE ID='{pk}';
        ''')
        messages.success(request, 'Produk berhasil dihapus')

    return redirect("/produk/list-produk")
