from .utils import get_query


def is_authenticated(request):
    '''Check if user in a session'''
    try:
        request.session["email"]
        return True
    except KeyError:
        return False


def get_role(email, password):
    admin_query = get_query(
        f'''
        SELECT email FROM admin WHERE email='{email}' AND password='{password}';
        '''
    )
    if type(admin_query) == list and len(admin_query) != 0:
        return "admin"

    user_query = get_query(
        f'''
        SELECT email FROM pengguna WHERE email='{email}' AND password='{password}';
        '''
    )
    if type(user_query) == list and len(user_query) != 0:
        return "user"

    return ""


def get_session_data(request):
    '''Get user session data'''
    if not is_authenticated(request):
        return {}

    try:
        return {"email": request.session["email"], "role": request.session["role"]}
    except:
        return {}
