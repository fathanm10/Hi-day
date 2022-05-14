from django.http import HttpResponse
from django.shortcuts import redirect, render
from hi_day.utils import get_query
from hi_day.auth import is_authenticated, get_role, get_session_data
from django.contrib import messages

def list_produk(request):
    if not is_authenticated(request):
        return redirect("/auth/login")