from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from hi_day.auth import is_authenticated, get_session_data, get_role
from hi_day.utils import get_query
from django.core.exceptions import PermissionDenied

def list_tipe_aset(request):
    if not is_authenticated(request):
        return redirect("/auth/login")

    data = get_session_data(request)
    return render(request, 'list_tipe_aset.html',{'title': 'Menu Lihat Aset', 'data': data})

def list_dekorasi(request):
    if not is_authenticated(request):
        return redirect("/auth/login")

    data = get_session_data(request)

    aset = get_query(
        f'''
        SELECT * FROM
        (SELECT ID, CASE
        WHEN ID IN (SELECT ID_ASET FROM KOLEKSI_ASET_MEMILIKI_ASET) THEN 'FALSE'
        WHEN ID IN (SELECT ID_BIBIT_TANAMAN FROM BIBIT_TANAMAN_MENGHASILKAN_HASIL_PANEN) THEN 'FALSE'
        WHEN ID IN (SELECT ID_HEWAN FROM HEWAN_MENGHASILKAN_PRODUK_HEWAN) THEN 'FALSE'
        WHEN ID IN (SELECT ID_ALAT_PRODUKSI FROM PRODUKSI) THEN 'FALSE'
        WHEN ID IN (SELECT ID_BIBIT_TANAMAN FROM HISTORI_TANAMAN) THEN 'FALSE'
        WHEN ID IN (SELECT ID_HEWAN FROM HISTORI_HEWAN) THEN 'FALSE'
        ELSE 'TRUE' END AS DELETABLE
        FROM ASET) AS A
        NATURAL JOIN
        (SELECT *
        FROM ASET JOIN DEKORASI
        ON ID=ID_ASET
        ORDER BY MIN_LEVEL) AS B;
        ''')

    return render(
        request, 'list_dekorasi.html',
        {
        'title': 'Dekorasi',
        'data': data,
        'aset': aset,
        })

def list_bibit_tanaman(request):
    if not is_authenticated(request):
        return redirect("/auth/login")
 
    data = get_session_data(request)
 
    aset = get_query(
        f'''
        SELECT * FROM
        (SELECT ID, CASE
        WHEN ID IN (SELECT ID_ASET FROM KOLEKSI_ASET_MEMILIKI_ASET) THEN 'FALSE'
        WHEN ID IN (SELECT ID_BIBIT_TANAMAN FROM BIBIT_TANAMAN_MENGHASILKAN_HASIL_PANEN) THEN 'FALSE'
        WHEN ID IN (SELECT ID_HEWAN FROM HEWAN_MENGHASILKAN_PRODUK_HEWAN) THEN 'FALSE'
        WHEN ID IN (SELECT ID_ALAT_PRODUKSI FROM PRODUKSI) THEN 'FALSE'
        WHEN ID IN (SELECT ID_BIBIT_TANAMAN FROM HISTORI_TANAMAN) THEN 'FALSE'
        WHEN ID IN (SELECT ID_HEWAN FROM HISTORI_HEWAN) THEN 'FALSE'
        ELSE 'TRUE' END AS DELETABLE
        FROM ASET) AS A
        NATURAL JOIN
        (SELECT *
        FROM ASET JOIN BIBIT_TANAMAN
        ON ID=ID_ASET
        ORDER BY MIN_LEVEL) AS B;
        ''')

    return render(
        request, 'list_bibit_tanaman.html',
        {
        'title': 'Bibit Tanaman',
        'data': data,
        'aset': aset,
        })

def list_kandang(request):
    if not is_authenticated(request):
        return redirect("/auth/login")
 
    data = get_session_data(request)
 
    aset = get_query(
        f'''
        SELECT * FROM
        (SELECT ID, CASE
        WHEN ID IN (SELECT ID_ASET FROM KOLEKSI_ASET_MEMILIKI_ASET) THEN 'FALSE'
        WHEN ID IN (SELECT ID_BIBIT_TANAMAN FROM BIBIT_TANAMAN_MENGHASILKAN_HASIL_PANEN) THEN 'FALSE'
        WHEN ID IN (SELECT ID_HEWAN FROM HEWAN_MENGHASILKAN_PRODUK_HEWAN) THEN 'FALSE'
        WHEN ID IN (SELECT ID_ALAT_PRODUKSI FROM PRODUKSI) THEN 'FALSE'
        WHEN ID IN (SELECT ID_BIBIT_TANAMAN FROM HISTORI_TANAMAN) THEN 'FALSE'
        WHEN ID IN (SELECT ID_HEWAN FROM HISTORI_HEWAN) THEN 'FALSE'
        ELSE 'TRUE' END AS DELETABLE
        FROM ASET) AS A
        NATURAL JOIN
        (SELECT *
        FROM ASET JOIN KANDANG
        ON ID=ID_ASET
        ORDER BY MIN_LEVEL) AS B;
        ''')

    return render(
        request, 'list_kandang.html',
        {
        'title': 'Kandang',
        'data': data,
        'aset': aset,
        })

def list_hewan(request):
    if not is_authenticated(request):
        return redirect("/auth/login")
 
    data = get_session_data(request)
 
    aset = get_query(
        f'''
        SELECT * FROM
        (SELECT ID, CASE
        WHEN ID IN (SELECT ID_ASET FROM KOLEKSI_ASET_MEMILIKI_ASET) THEN 'FALSE'
        WHEN ID IN (SELECT ID_BIBIT_TANAMAN FROM BIBIT_TANAMAN_MENGHASILKAN_HASIL_PANEN) THEN 'FALSE'
        WHEN ID IN (SELECT ID_HEWAN FROM HEWAN_MENGHASILKAN_PRODUK_HEWAN) THEN 'FALSE'
        WHEN ID IN (SELECT ID_ALAT_PRODUKSI FROM PRODUKSI) THEN 'FALSE'
        WHEN ID IN (SELECT ID_BIBIT_TANAMAN FROM HISTORI_TANAMAN) THEN 'FALSE'
        WHEN ID IN (SELECT ID_HEWAN FROM HISTORI_HEWAN) THEN 'FALSE'
        ELSE 'TRUE' END AS DELETABLE
        FROM ASET) AS A
        NATURAL JOIN
        (SELECT *
        FROM ASET JOIN HEWAN
        ON ID=ID_ASET
        ORDER BY MIN_LEVEL) AS B;
        ''')

    return render(
        request, 'list_hewan.html',
        {
        'title': 'Hewan',
        'data': data,
        'aset': aset,
        })

def list_alat_produksi(request):
    if not is_authenticated(request):
        return redirect("/auth/login")
 
    data = get_session_data(request)
 
    aset = get_query(
        f'''
        SELECT * FROM
        (SELECT ID, CASE
        WHEN ID IN (SELECT ID_ASET FROM KOLEKSI_ASET_MEMILIKI_ASET) THEN 'FALSE'
        WHEN ID IN (SELECT ID_BIBIT_TANAMAN FROM BIBIT_TANAMAN_MENGHASILKAN_HASIL_PANEN) THEN 'FALSE'
        WHEN ID IN (SELECT ID_HEWAN FROM HEWAN_MENGHASILKAN_PRODUK_HEWAN) THEN 'FALSE'
        WHEN ID IN (SELECT ID_ALAT_PRODUKSI FROM PRODUKSI) THEN 'FALSE'
        WHEN ID IN (SELECT ID_BIBIT_TANAMAN FROM HISTORI_TANAMAN) THEN 'FALSE'
        WHEN ID IN (SELECT ID_HEWAN FROM HISTORI_HEWAN) THEN 'FALSE'
        ELSE 'TRUE' END AS DELETABLE
        FROM ASET) AS A
        NATURAL JOIN
        (SELECT *
        FROM ASET JOIN ALAT_PRODUKSI
        ON ID=ID_ASET
        ORDER BY MIN_LEVEL) AS B;
        ''')

    return render(
        request, 'list_alat_produksi.html',
        {
        'title': 'Alat Produksi',
        'data': data,
        'aset': aset,
        })

def list_petak_sawah(request):
    if not is_authenticated(request):
        return redirect("/auth/login")
 
    data = get_session_data(request)
 
    aset = get_query(
        f'''
        SELECT * FROM
        (SELECT ID, CASE
        WHEN ID IN (SELECT ID_ASET FROM KOLEKSI_ASET_MEMILIKI_ASET) THEN 'FALSE'
        WHEN ID IN (SELECT ID_BIBIT_TANAMAN FROM BIBIT_TANAMAN_MENGHASILKAN_HASIL_PANEN) THEN 'FALSE'
        WHEN ID IN (SELECT ID_HEWAN FROM HEWAN_MENGHASILKAN_PRODUK_HEWAN) THEN 'FALSE'
        WHEN ID IN (SELECT ID_ALAT_PRODUKSI FROM PRODUKSI) THEN 'FALSE'
        WHEN ID IN (SELECT ID_BIBIT_TANAMAN FROM HISTORI_TANAMAN) THEN 'FALSE'
        WHEN ID IN (SELECT ID_HEWAN FROM HISTORI_HEWAN) THEN 'FALSE'
        ELSE 'TRUE' END AS DELETABLE
        FROM ASET) AS A
        NATURAL JOIN
        (SELECT *
        FROM ASET JOIN PETAK_SAWAH
        ON ID=ID_ASET
        ORDER BY MIN_LEVEL) AS B;
        ''')

    return render(
        request, 'list_petak_sawah.html',
        {
        'title': 'Petak Sawah',
        'data': data,
        'aset': aset,
        })

















def list_koleksi_aset(request):
    if not is_authenticated(request):
        return redirect("/auth/login")

    data = get_session_data(request)
    return render(request, 'list_koleksi_aset.html', {'title': 'Menu Lihat Koleksi Aset', 'data': data})

def list_koleksi_dekorasi(request):
    if not is_authenticated(request):
        return redirect("/auth/login")

    data = {}
    data['role'] = get_role(request.session['email'], request.session['password'])

    if (data['role'] == 'admin'):
        result = get_query(
            f'''
            SELECT * FROM
            (SELECT ID_KOLEKSI_ASET, ID_ASET AS C, JUMLAH
            FROM KOLEKSI_ASET_MEMILIKI_ASET) AS A
            JOIN
            (SELECT *
            FROM ASET JOIN DEKORASI
            ON ID=ID_ASET) AS B
            ON C = ID;
            ''')
    elif (data['role'] == 'user'):
        result = get_query(
            f'''
            SELECT * FROM
            (SELECT ID_KOLEKSI_ASET, ID_ASET AS C, JUMLAH
            FROM KOLEKSI_ASET_MEMILIKI_ASET
            WHERE ID_KOLEKSI_ASET='{request.session['email']}') AS A
            JOIN
            (SELECT *
            FROM ASET JOIN DEKORASI
            ON ID=ID_ASET) AS B
            ON C = ID;
            ''')

    return render(
        request,
        'list_koleksi_dekorasi.html',
        {'title': 'Koleksi Dekorasi', 'data': data, 'result': result})

def list_koleksi_bibit_tanaman(request):
    if not is_authenticated(request):
        return redirect("/auth/login")

    data = {}
    data['role'] = get_role(request.session['email'], request.session['password'])

    if (data['role'] == 'admin'):
        result = get_query(
            f'''
            SELECT * FROM
            (SELECT ID_KOLEKSI_ASET, ID_ASET AS C, JUMLAH
            FROM KOLEKSI_ASET_MEMILIKI_ASET) AS A
            JOIN
            (SELECT *
            FROM ASET JOIN BIBIT_TANAMAN
            ON ID=ID_ASET) AS B
            ON C = ID;
            ''')
    elif (data['role'] == 'user'):
        result = get_query(
            f'''
            SELECT * FROM
            (SELECT ID_KOLEKSI_ASET, ID_ASET AS C, JUMLAH
            FROM KOLEKSI_ASET_MEMILIKI_ASET
            WHERE ID_KOLEKSI_ASET='{request.session['email']}') AS A
            JOIN
            (SELECT *
            FROM ASET JOIN BIBIT_TANAMAN
            ON ID=ID_ASET) AS B
            ON C = ID;
            ''')

    return render(
        request,
        'list_koleksi_bibit_tanaman.html',
        {'title': 'Koleksi Bibit Tanaman', 'data': data, 'result': result})

def list_koleksi_kandang(request):
    if not is_authenticated(request):
        return redirect("/auth/login")

    data = {}
    data['role'] = get_role(request.session['email'], request.session['password'])

    if (data['role'] == 'admin'):
        result = get_query(
            f'''
            SELECT * FROM
            (SELECT ID_KOLEKSI_ASET, ID_ASET AS C, JUMLAH
            FROM KOLEKSI_ASET_MEMILIKI_ASET) AS A
            JOIN
            (SELECT *
            FROM ASET JOIN KANDANG
            ON ID=ID_ASET) AS B
            ON C = ID;
            ''')
    elif (data['role'] == 'user'):
        result = get_query(
            f'''
            SELECT * FROM
            (SELECT ID_KOLEKSI_ASET, ID_ASET AS C, JUMLAH
            FROM KOLEKSI_ASET_MEMILIKI_ASET
            WHERE ID_KOLEKSI_ASET='{request.session['email']}') AS A
            JOIN
            (SELECT *
            FROM ASET JOIN KANDANG
            ON ID=ID_ASET) AS B
            ON C = ID;
            ''')

    return render(
        request,
        'list_koleksi_kandang.html',
        {'title': 'Koleksi Kandang', 'data': data, 'result': result})

def list_koleksi_hewan(request):
    if not is_authenticated(request):
        return redirect("/auth/login")

    data = {}
    data['role'] = get_role(request.session['email'], request.session['password'])

    if (data['role'] == 'admin'):
        result = get_query(
            f'''
            SELECT * FROM
            (SELECT ID_KOLEKSI_ASET, ID_ASET AS C, JUMLAH
            FROM KOLEKSI_ASET_MEMILIKI_ASET) AS A
            JOIN
            (SELECT *
            FROM ASET JOIN HEWAN
            ON ID=ID_ASET) AS B
            ON C = ID;
            ''')
    elif (data['role'] == 'user'):
        result = get_query(
            f'''
            SELECT * FROM
            (SELECT ID_KOLEKSI_ASET, ID_ASET AS C, JUMLAH
            FROM KOLEKSI_ASET_MEMILIKI_ASET
            WHERE ID_KOLEKSI_ASET='{request.session['email']}') AS A
            JOIN
            (SELECT *
            FROM ASET JOIN HEWAN
            ON ID=ID_ASET) AS B
            ON C = ID;
            ''')

    return render(
        request,
        'list_koleksi_hewan.html',
        {'title': 'Koleksi Hewan', 'data': data, 'result': result})

def list_koleksi_alat_produksi(request):
    if not is_authenticated(request):
        return redirect("/auth/login")

    data = {}
    data['role'] = get_role(request.session['email'], request.session['password'])

    if (data['role'] == 'admin'):
        result = get_query(
            f'''
            SELECT * FROM
            (SELECT ID_KOLEKSI_ASET, ID_ASET AS C, JUMLAH
            FROM KOLEKSI_ASET_MEMILIKI_ASET) AS A
            JOIN
            (SELECT *
            FROM ASET JOIN ALAT_PRODUKSI
            ON ID=ID_ASET) AS B
            ON C = ID;
            ''')
    elif (data['role'] == 'user'):
        result = get_query(
            f'''
            SELECT * FROM
            (SELECT ID_KOLEKSI_ASET, ID_ASET AS C, JUMLAH
            FROM KOLEKSI_ASET_MEMILIKI_ASET
            WHERE ID_KOLEKSI_ASET='{request.session['email']}') AS A
            JOIN
            (SELECT *
            FROM ASET JOIN ALAT_PRODUKSI
            ON ID=ID_ASET) AS B
            ON C = ID;
            ''')

    return render(
        request,
        'list_koleksi_alat_produksi.html',
        {'title': 'Koleksi Alat Produksi', 'data': data, 'result': result})

def list_koleksi_petak_sawah(request):
    if not is_authenticated(request):
        return redirect("/auth/login")

    data = {}
    data['role'] = get_role(request.session['email'], request.session['password'])

    if (data['role'] == 'admin'):
        result = get_query(
            f'''
            SELECT * FROM
            (SELECT ID_KOLEKSI_ASET, ID_ASET AS C, JUMLAH
            FROM KOLEKSI_ASET_MEMILIKI_ASET) AS A
            JOIN
            (SELECT *
            FROM ASET JOIN PETAK_SAWAH
            ON ID=ID_ASET) AS B
            ON C = ID;
            ''')
    elif (data['role'] == 'user'):
        result = get_query(
            f'''
            SELECT * FROM
            (SELECT ID_KOLEKSI_ASET, ID_ASET AS C, JUMLAH
            FROM KOLEKSI_ASET_MEMILIKI_ASET
            WHERE ID_KOLEKSI_ASET='{request.session['email']}') AS A
            JOIN
            (SELECT *
            FROM ASET JOIN PETAK_SAWAH
            ON ID=ID_ASET) AS B
            ON C = ID;
            ''')

    return render(
        request,
        'list_koleksi_petak_sawah.html',
        {'title': 'Koleksi Petak Sawah', 'data': data, 'result': result})

def list_transaksi_pembelian_aset(request):
    if not is_authenticated(request):
        return redirect("/auth/login")

    data = {}
    data['role'] = get_role(request.session['email'], request.session['password'])

    if (data['role'] == 'admin'):
        result = get_query(
            f'''
            SELECT EMAIL, WAKTU,
            CASE
                WHEN ID LIKE 'd%' THEN 'Dekorasi'
                WHEN ID LIKE 'bt%' THEN 'Bibit Tanaman'
                WHEN ID LIKE 'k%' THEN 'Kandang'
                WHEN ID LIKE 'h%' THEN 'Hewan'
                WHEN ID LIKE 'ap%' THEN 'Alat Produksi'
                WHEN ID LIKE 'ps%' THEN 'Petak Sawah'
            END JENIS,
            NAMA, JUMLAH, JUMLAH*HARGA_BELI AS TOTAL_HARGA
            FROM
            (SELECT *
            FROM TRANSAKSI_PEMBELIAN) AS A
            JOIN
            (SELECT *
            FROM ASET) AS B
            ON ID=ID_ASET;
            ''')
    elif (data['role'] == 'user'):
        result = get_query(
            f'''
            SELECT EMAIL, WAKTU,
            CASE
                WHEN ID LIKE 'd%' THEN 'Dekorasi'
                WHEN ID LIKE 'bt%' THEN 'Bibit Tanaman'
                WHEN ID LIKE 'k%' THEN 'Kandang'
                WHEN ID LIKE 'h%' THEN 'Hewan'
                WHEN ID LIKE 'ap%' THEN 'Alat Produksi'
                WHEN ID LIKE 'ps%' THEN 'Petak Sawah'
            END JENIS,
            NAMA, JUMLAH, JUMLAH*HARGA_BELI AS TOTAL_HARGA
            FROM
            (SELECT *
            FROM TRANSAKSI_PEMBELIAN
            WHERE EMAIL='{request.session['email']}') AS A
            JOIN
            (SELECT *
            FROM ASET) AS B
            ON ID=ID_ASET;
            ''')

    return render(
        request,
        'list_transaksi_pembelian_aset.html',
        {'title': 'Transaksi Pembelian Aset', 'data': data, 'result': result})












def create_aset_list(request):
    if not is_authenticated(request):
        return redirect("/auth/login")
    
    print('masuk')
    data = get_session_data(request)
    return render(
        request,
        'create_aset_list.html',
        {'title': 'Menu Buat Aset', 'data': data})

@csrf_exempt
def create_dekorasi(request):
    if not is_authenticated(request):
        return redirect("/auth/login")

    data = get_session_data(request)
    if request.method != "POST":
        return render(request, 'create_dekorasi.html',
        {
            'title': "Dekorasi",
            'data': data
        })

    print('do stuff')

@csrf_exempt
def create_bibit_tanaman(request):
    if not is_authenticated(request):
        return redirect("/auth/login")

    data = get_session_data(request)
    if request.method != "POST":
        return render(request, 'create_bibit_tanaman.html',
        {
            'title': "Bibit Tanaman",
            'data': data
        })

    print('do stuff')

@csrf_exempt
def create_kandang(request):
    if not is_authenticated(request):
        return redirect("/auth/login")

    data = get_session_data(request)
    if request.method != "POST":
        return render(request, 'create_kandang.html',
        {
            'title': "Kandang",
            'data': data
        })

    print('masuk')

@csrf_exempt
def create_hewan(request):
    if not is_authenticated(request):
        return redirect("/auth/login")

    data = get_session_data(request)
    if request.method != "POST":
        return render(request, 'create_hewan.html',
        {
            'title': "Hewan",
            'data': data
        })

    print('do stuff')

@csrf_exempt
def create_alat_produksi(request):
    if not is_authenticated(request):
        return redirect("/auth/login")

    data = get_session_data(request)
    if request.method != "POST":
        return render(request, 'create_alat_produksi.html',
        {
            'title': "Alat Produksi",
            'data': data
        })

    print('do stuff')

@csrf_exempt
def create_petak_sawah(request):
    if not is_authenticated(request):
        return redirect("/auth/login")

    data = get_session_data(request)
    if request.method != "POST":
        return render(request, 'create_petak_sawah.html',
        {
            'title': "Petak Sawah",
            'data': data
        })

    print('do stuff')

@csrf_exempt
def create_transaksi_beli_aset(request):
    if not is_authenticated(request):
        return redirect("/auth/login")

    data = get_session_data(request)
    if request.method != "POST":
        return render(request, 'create_transaksi_beli_aset.html',
        {
            'title': "Menu Buat Transaksi Pembelian Aset",
            'data': data
        })

    print('do stuff')










@csrf_exempt
def update_dekorasi(request, id):
    print('do stuff')

@csrf_exempt
def update_bibit_tanaman(request, id):
    print('do stuff')

@csrf_exempt
def update_kandang(request, id):
    print('do stuff')

@csrf_exempt
def update_hewan(request, id):
    print('do stuff')

@csrf_exempt
def update_alat_produksi(request, id):
    print('do stuff')

@csrf_exempt
def update_petak_sawah(request, id):
    print('do stuff')





id_to_aset = {'ap': 'ALAT_PRODUKSI', 'bt': 'BIBIT_TANAMAN', 'd': 'DEKORASI', 'h': 'HEWAN', 'k': 'KANDANG', 'ps': 'PETAK_SAWAH'}

@csrf_exempt
def delete_aset(request, id):
    if get_session_data(request)['role'] == 'user':
        raise PermissionDenied()
    
    if get_session_data(request)['role'] == 'admin':
        tipe_aset = ''
        if ('ap' in id):
            tipe_aset = id_to_aset['ap']
        elif ('bt' in id):
            tipe_aset = id_to_aset['bt']
        elif ('d' in id):
            tipe_aset = id_to_aset['d']
        elif ('h' in id):
            tipe_aset = id_to_aset['h']
        elif ('k' in id):
            tipe_aset = id_to_aset['k']
        elif ('ps' in id):
            tipe_aset = id_to_aset['ps']
        else:
            return redirect("/")

        get_query(
            f'''
            DELETE FROM {tipe_aset} WHERE ID_ASET = '{id}';
            DELETE FROM ASET WHERE ID = '{id}';
            ''')

        return redirect("/")