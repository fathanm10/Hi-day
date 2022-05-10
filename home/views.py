from django.shortcuts import redirect, render
from hi_day.utils import get_query
from hi_day.auth import is_authenticated, get_role, get_session_data


def index(request):
    if not is_authenticated(request):
        return redirect("/auth/login")
    user_data = get_session_data(request)

    return render(request, 'home/index.html', {'title': "Home", 'data':user_data})
