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

    # print(result[1])

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
        ON PM.ID = PPM.ID_produk
        WHERE PPM.ID_produk_makanan='{produk_makanan}';
    ''')
    print(result)
    print(component)

    bahan = []
    for i in range(len(component)):
        bahan.append({
            "nama": component[i][0],
            "jumlah": component[i][1],
        })

    production_data = {
        "nama": result[0][0],
        "alat": result[0][1],
        "durasi": str(result[0][2]),
        "jumlah": result[0][3],
        "bahan": bahan,
    }

    data['production'] = production_data

    return render(request, 'produksi/detail_produksi.html', {'title': production_data['nama'], 'data': data})


def buat_produksi(request):
    data = {}
    data['role'] = get_role(request.session['email'],
                            request.session['password'])
    data['user'] = get_session_data(request)

    data_makanan = get_query('''
        SELECT P.nama, P.ID
        FROM produk AS P
        INNER JOIN produk_makanan AS PM
        ON PM.ID_Produk = P.ID;
    ''')

    data_alat = get_query('''
        SELECT A.nama, A.ID
        FROM aset AS A
        INNER JOIN alat_produksi AS AP
        ON AP.ID_aset = A.ID;
    ''')

    data_produk = get_query('''
        SELECT P.nama, P.ID
        FROM produk AS P;
    ''')

    data['production'] = {}
    makanan = []
    alat = []
    produk = []
    for i in range(len(data_makanan)):
        makanan.append({
            "nama": data_makanan[i][0],
            "id": data_makanan[i][1],
        })
    for i in range(len(data_alat)):
        alat.append({
            "nama": data_alat[i][0],
            "id": data_alat[i][1],
        })
    for i in range(len(data_produk)):
        produk.append({
            "nama": data_produk[i][0],
            "id": data_produk[i][1],
        })

    data['production']['makanan'] = makanan
    data['production']['alat'] = alat
    data['production']['produk'] = produk

    if request.method != "POST":
        if not is_authenticated(request):
            return redirect("/auth/login")
        return render(request, 'produksi/add_produksi.html', {'title': "Buat Produksi", 'data': data})

    body = request.POST
    makanan = body['makanan']
    alat = body['alat']
    durasi = f"00:{body['durasi']}:00"
    jumlah = body['jumlah']

    bahanList = list(body.values())[7:-1]
    bahan = {}
    i = 0
    j = 1
    while i < len(bahanList):
        bahan["bahan" + str(j)] = {}
        bahan["bahan" + str(j)]["bahan"] = bahanList[i]
        bahan["bahan" + str(j)]["jumlahBahan"] = bahanList[i + 1]
        i += 2
        j += 1

    get_query(f'''
        INSERT INTO produksi
        VALUES ('{alat}', '{makanan}', '{durasi}', '{jumlah}');
    ''')

    for i in bahan:
        id_bahan = get_query(f'''
            SELECT ID FROM produk WHERE nama='{bahan[i]['bahan']}';
        ''')

        get_query(f'''
            INSERT INTO produk_dibutuhkan_oleh_produk_makanan
            VALUES ('{makanan}', '{id_bahan[0][0]}', '{bahan[i]['jumlahBahan']}');
        ''')

    return redirect("/produksi/list-produksi")


def update_produksi(request, pk):
    if not is_authenticated(request):
        return redirect("/auth/login")

    data = {}
    data['role'] = get_role(request.session['email'],
                            request.session['password'])
    data['user'] = get_session_data(request)

    produk_makanan = pk.split("-")[0]
    alat_produksi = pk.split("-")[1]

    data_production = get_query(f'''
        SELECT PM.nama AS makanan, A.nama AS alat, PR.durasi, PR.jumlah_hasil_unit
        FROM produksi AS PR
        INNER JOIN produk AS PM
        ON PM.ID = PR.ID_produk_makanan
        INNER JOIN aset AS A
        ON A.ID = PR.ID_alat_produksi
        WHERE PR.ID_produk_makanan='{produk_makanan}' AND PR.ID_alat_produksi='{alat_produksi}';
    ''')

    data_bahan = get_query(f'''
        SELECT PM.nama, PPM.jumlah
        FROM produk_dibutuhkan_oleh_produk_makanan AS PPM
        INNER JOIN produk AS PM
        ON PM.ID = PPM.ID_produk
        WHERE PPM.ID_produk_makanan='{produk_makanan}';
    ''')

    bahan = []
    for i in range(len(data_bahan)):
        bahan.append({
            'nama': data_bahan[i][0],
            'jumlah': data_bahan[i][1],
        })

    data['production'] = {
        'makanan': data_production[0][0],
        'alat': data_production[0][1],
        'durasi': str(data_production[0][2])[3:5],
        'jumlah': data_production[0][3],
        'bahan': bahan
    }

    if request.method != "POST":
        return render(request, 'produksi/update_produksi.html', {'title': ("Update Produksi " + data['production']['makanan']), 'data': data})

    body = request.POST
    durasi = f"00:{body['durasi']}:00"
    jumlah = body['jumlah']

    get_query(f'''
        UPDATE produksi
        SET durasi='{durasi}', jumlah_hasil_unit='{jumlah}'
        WHERE ID_produk_makanan='{produk_makanan}' AND ID_alat_produksi='{alat_produksi}';
    ''')

    return redirect("/produksi/list-produksi")


def delete_produksi(request, pk):
    if not is_authenticated(request):
        return redirect("/auth/login")

    data = {}
    data['role'] = get_role(request.session['email'],
                            request.session['password'])
    data['user'] = get_session_data(request)

    if data['role'] != 'admin':
        return redirect("/produk/list-produk")

    produk_makanan = pk.split("-")[0]
    alat_produksi = pk.split("-")[1]

    history_data = get_query(f'''
        SELECT id_produk_makanan, id_alat_produksi
        FROM histori_produksi_makanan
        WHERE id_produk_makanan='{produk_makanan}' AND id_alat_produksi='{alat_produksi}';
    ''')
    # print(history_data)

    if(len(history_data) != 0):
        messages.error(request, 'Produksi tidak bisa dihapus')
    else:
        get_query(f'''
            DELETE FROM produksi CASCADE
            WHERE id_produk_makanan='{produk_makanan}' AND id_alat_produksi='{alat_produksi}';
        ''')
        messages.success(request, 'Produksi berhasil dihapus')

    return redirect("/produksi/list-produksi")
