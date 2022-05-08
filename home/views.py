from django.shortcuts import render
from django.db import connection
from collections import namedtuple

def index(request):
    cursor = connection.cursor()
    result = []
    try:
        cursor.execute("SET SEARCH_PATH TO hi_day")
        cursor.execute("SELECT email FROM akun") # Just an example
        result = namedtuplefetchall(cursor)
        print(result)
    except Exception as e:
        print(e)
    finally:
        cursor.close()

    return render(request, 'home/index.html', {'title':"Home", 'result': result})


def namedtuplefetchall(cursor):
    "Return all rows from a cursor as a namedtuple"
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]