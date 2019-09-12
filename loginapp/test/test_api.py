import requests

def test_login():
    data = {
        'u_phone': '15212345678',
        'auth_string': '123456'
    }
    resp = requests.post('http://localhost:8000/login/login/', json=data)
    print(resp.json())


if __name__ == '__main__':
    test_login()