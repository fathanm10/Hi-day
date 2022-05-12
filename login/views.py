from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

from hi_day.utils import get_query
from hi_day.auth import is_authenticated, get_role, get_session_data


def index(request):
    if is_authenticated(request):
        return redirect("/")
    return render(request, 'login/index.html', {'title': "Masuk"})


@csrf_exempt
def login(request):
    next = request.GET.get("next")

    if request.method != "POST":
        if is_authenticated(request):
            return redirect("/")
        return render(request, 'login/login.html', {'title': "Login"})

    if is_authenticated(request):
        email = str(request.session["email"])
        password = str(request.session["password"])
    else:
        email = str(request.POST["email"])
        password = str(request.POST["password"])

    user = get_query(f'''
    SELECT email FROM admin WHERE email='{email}' AND password='{password}';
    ''')

    role = get_role(email, password)

    if role == "":
        if is_authenticated(request):
            return redirect("/")
        messages.error(request, 'Email atau password salah')
        return render(request, 'login/login.html', {'title': "Login"})
    else:
        request.session["email"] = email
        request.session["password"] = password
        request.session["role"] = role
        request.session.set_expiry(0)
        request.session.modified = True

        if next != None and next != "None":
            return redirect(next)
        else:
            return redirect("/")


def logout(request):
    next = request.GET.get("next")

    if not is_authenticated(request):
        return redirect("/auth/login")

    request.session.flush()
    request.session.clear_expired()

    if next != None and next != "None":
        return redirect(next)
    else:
        return redirect("/auth/login")


@csrf_exempt
def register(request):
    next = request.GET.get("next")

    if is_authenticated(request):
        return redirect("/")

    return render(request, 'login/register.html', {'title': "Register"})


@csrf_exempt
def register_admin(request):
    next = request.GET.get("next")

    if request.method != "POST":
        if is_authenticated(request):
            return redirect("/")
        return render(request, 'login/register_admin.html', {'title': "Register Admin"})

    body = request.POST

    email = body['email']
    password = body['password']

    result = get_query(
        f"""
        INSERT INTO akun VALUES
        ('{email}');

        INSERT INTO admin VALUES
        ('{email}', '{password}');
        """
    )

    role = get_role(email, password)

    if role == "":
        if is_authenticated(request):
            return redirect("/")
        messages.error(request, 'Email sudah dipakai')
        return render(request, 'login/register_admin.html', {'title': "Register Admin"})

    request.session["email"] = email
    request.session["password"] = password
    request.session["role"] = "admin"
    request.session.set_expiry(0)
    request.session.modified = True

    if next != None and next != "None":
        return redirect(next)
    else:
        return redirect("/")

@csrf_exempt
def register_user(request):
    next = request.GET.get("next")

    if request.method != "POST":
        if is_authenticated(request):
            return redirect("/")
        return render(request, 'login/register_user.html', {'title': "Register User"})

    body = request.POST

    email = body['email']
    password = body['password']
    farm = body['farm']

    result = get_query(
        f"""
        INSERT INTO akun VALUES
        ('{email}');

        INSERT INTO pengguna VALUES
        ('{email}', '{password}', '{farm}');
        """
    )

    role = get_role(email, password)

    if role == "":
        if is_authenticated(request):
            return redirect("/")
        messages.error(request, 'Email sudah dipakai')
        return render(request, 'login/register_user.html', {'title': "Register User"})

    request.session["email"] = email
    request.session["password"] = password
    request.session["role"] = "user"
    request.session.set_expiry(0)
    request.session.modified = True

    if next != None and next != "None":
        return redirect(next)
    else:
        return redirect("/")
