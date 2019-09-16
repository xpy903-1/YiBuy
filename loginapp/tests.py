import requests
from django.test import TestCase


# Create your tests here.

def test_login():
    data = {
        'u_phone': '15212345678',
        'auth_string': '123456'
    }

    resp = requests.post('http://localhost:8000/login/login/', json=data)
    print(resp.json())


def test_check():
    data = {
        'phone': '13619254683'
    }

    resp = requests.get('http://localhost:8000/login/check/', json=data)
    print(resp.json())


if __name__ == '__main__':
    test_login()
    test_check()
