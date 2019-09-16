import requests


def test_query():
    data = {
        'name': 'bob'
    }
    resp = requests.post('http://localhost:8000/address/query/',
                         json=data)
    print(resp.json())


if __name__ == '__main__':
    test_query()



def test_add():
    data = {
        'user_id': '8370030c-a3ef-4ff3-8c8b-7005e680120a',
        'name': '小明',
        'phone': '15236546987',
        'ads': '宝鸡市世纪大道'
    }
    resp = requests.post('http://localhost:8000/address/add/',
                         json=data)
    print(resp.json())

if __name__ == '__main__':
    test_add()



def test_edit():
    data = {
        'id': 'd6b65fe8-d93e-4612-b8b9-cda783c3a0ea',
        'name': '李四',
        'phone':'12345678912',
        'ads':'西安市雁塔区'
    }
    resp = requests.post('http://localhost:8000/address/edit/',
                         json=data)
    print(resp.json())

if __name__ == '__main__':
    test_edit()



def test_delete():
    data = {
        'id': '',

    }
    resp = requests.post('http://localhost:8000/address/delete/',
                         json=data)
    print(resp.json())

if __name__ == '__main__':
    test_delete()
