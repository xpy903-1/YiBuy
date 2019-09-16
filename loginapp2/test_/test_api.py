import requests
import unittest
from unittest import  TestCase

from requests import post


class Login_Case(TestCase):
    def test_01_login(self):
        data = {
            'u_phone': '13470061772',
            'auth_string': '031837'
        }
        resp = requests.post('http://localhost:8000/login/login/', json=data)
        print(resp.json())

    def test_02(self):
        url = 'http://localhost:8000/login2/upload/'
        with open('D:\codes\YiBuy\media\imags\lu.jpg','rb') as f:
            a = f.read()

        files = {'name': a}
        resp = requests.request(method='post', url=url, files=files)
        print(resp)
    # def test_detaios():
    #     resp = requests.post('http://localhost:8000/login2/detaios/')
    #     print(resp.json())
    #
    #
    #
    # def test_loginout():
    #     resp = requests.get('http://localhost:8000/login2/loginout/')
    #     print(resp.json())
    #     requests.request()
    #
    # def test_change():
    #     data: {
    #         'user_name': '东',
    #         'user_phone': '13470016772',
    #         'user_pwd': '14740557360'
    #     }
    #     resp = requests.post('http://localhost:8000/login2/change/', join=data)
    #     print(resp.json())
    #
    #
    #
    # def test_imgurl():
    #     resp = requests.get('http://localhost:8000/login2/imgurl')
    #     print(resp.json())
