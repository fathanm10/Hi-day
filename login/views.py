from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt

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
        return render(request, 'login/login.html')

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
        return render(request, 'login/login.html')
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


def register(request):
    result = get_query('''
    SELECT * FROM akun;
    ''')
    print(result)

    return render(request, 'login/register.html', {'title': "Register", 'result': result})
