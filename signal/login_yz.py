
def login_yz_fun(sender, **kwargs):
    request = kwargs['request']
    token = request.COOKIES.get('token')
    print(token)
    if token:
        uid = request.session.get(token, None)
        print(uid)
        if not uid:
            return False
        else:
            return uid
    else:
        return False