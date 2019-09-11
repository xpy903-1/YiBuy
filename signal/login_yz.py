
def login_yz_fun(sender, **kwargs):
    request = kwargs['request']
    token = request.COOKIES.get('token')
    print(token)
    if token:
        uid = request.session[token]
        print(not uid)
        if not uid:
            return False
        else:
            return True
    else:
        return False