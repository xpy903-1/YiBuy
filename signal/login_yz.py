
def login_yz_fun(sender, **kwargs):
    request = kwargs['request']
    token = request.COOKIES.get('token')
    if token:
        uid = request.session[token]
        print(not uid)
        if not uid:
            return False
        else:
            return uid
    else:
        return False