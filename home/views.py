from django.shortcuts import redirect, render
from hi_day.utils import get_query
from hi_day.auth import is_authenticated, get_role, get_session_data


def index(request):
    if not is_authenticated(request):
        return redirect("/auth/login")
    
    data = {}
    data['role'] = get_role(request.session['email'], request.session['password'])
    
    user_data = {}
    if (data['role'] == 'admin'):
        user_data = get_session_data(request)
    elif (data['role'] == 'user'):
        result = get_query(f'''
            SELECT * FROM pengguna
            WHERE email='{request.session['email']}';
        ''')
        print(result[0])
        user_data['email'] = result[0][0]
        user_data['farm'] = result[0][2]
        user_data['xp'] = result[0][3]
        user_data['koin'] = result[0][4]
        user_data['level'] = result[0][5]

    
    data['user'] = user_data

    # print(data)

    return render(request, 'home/index.html', {'title': "Home", 'data':data})
