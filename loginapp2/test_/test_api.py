import requests



def test_detaios():
    resp = requests.post('http://localhost:8000/login2/detaios/')
    print(resp.json())



def test_loginout():
    resp = requests.get('http://localhost:8000/login2/loginout/')
    print(resp.json())


def test_change():
    data: {
        'user_name': '东',
        'user_phone': '13470016772',
        'user_pwd': '14740557360'
    }
    resp = requests.post('http://localhost:8000/login2/change/', join=data)
    print(resp.json())



def test_imgurl():
    resp = requests.get('http://localhost:8000/login2/imgurl')
    print(resp.json())

if __name__ == '__main__':
    test_loginout()