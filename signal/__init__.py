from django import dispatch

from signal.login_yz import login_yz_fun

login_yz = dispatch.Signal(providing_args=['request'])

login_yz.connect(login_yz_fun)