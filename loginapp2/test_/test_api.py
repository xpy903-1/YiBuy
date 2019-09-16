import uuid

import requests
from unittest import TestSuite, TextTestRunner, TestCase


class Login_Case(TestCase):
    token = 1
    def test_01_login(self):
        data = {
            'u_phone': '13470016772',
            'auth_string': '14740557360'
        }

        resp = requests.post('http://localhost:8000/login/login/', json=data)

        print(resp.json())
        Login_Case.token = resp.json()['token']

    def test_02_detaios(self):
        data = {
            'user_id': Login_Case.token
        }

        resp = requests.post('http://localhost:8000/login2/detaios/', json=data)
        print(resp.json())

    def test_03_change(self):
        data = {
            'user_id': Login_Case.token,
            'user_name': '东',
            'user_phone': '13470009372',
            'user_pwd': '1474055'
        }
        resp = requests.post('http://localhost:8000/login2/change/', json=data)
        print(resp.json())

    def test_04_imgurl(self):
        resp = requests.get('http://localhost:8000/login2/imgurl')
        print(resp.json())

    def test_05_loginout(self):
        resp = requests.get('http://localhost:8000/login2/loginout/')
        print(resp.json())


def suite1():
    suite_ = TestSuite()

    suite_.addTest(Login_Case.test_01_login)
    suite_.addTest(Login_Case.test_02_detaios)
    suite_.addTest(Login_Case.test_03_change)
    suite_.addTest(Login_Case.test_04_imgurl)
    suite_.addTest(Login_Case.test_05_loginout)

    return suite_


if __name__ == '__main__':
    TextTestRunner().run(TestSuite(suite1()))
