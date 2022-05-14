from django.shortcuts import render, redirect

from hi_day.auth import is_authenticated, get_session_data, get_role
from hi_day.utils import get_query

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
        SELECT *
        FROM ASET JOIN DEKORASI
        ON ID=ID_ASET
        ORDER BY MIN_LEVEL;
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
        SELECT *
        FROM ASET JOIN BIBIT_TANAMAN
        ON ID=ID_ASET
        ORDER BY MIN_LEVEL;
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
        SELECT *
        FROM ASET JOIN KANDANG
        ON ID=ID_ASET
        ORDER BY MIN_LEVEL;
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
        SELECT *
        FROM ASET JOIN HEWAN
        ON ID=ID_ASET
        ORDER BY MIN_LEVEL;
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
        SELECT *
        FROM ASET JOIN ALAT_PRODUKSI
        ON ID=ID_ASET
        ORDER BY MIN_LEVEL;
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
        SELECT *
        FROM ASET JOIN PETAK_SAWAH
        ON ID=ID_ASET
        ORDER BY MIN_LEVEL;
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