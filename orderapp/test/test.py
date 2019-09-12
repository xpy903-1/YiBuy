import requests


def test_asd():
    resp = requests.get('http://localhost:8000/order/list/1eac57c459b44269b0186d2748f2e70a/1')
    # resp = requests.get('http://localhost/order/list/')
    print(resp.json())

def test_asd1():
    resp = requests.get('http://localhost:8000/order/home/302f3970d25448c6920817e5ea61e88d')
    # resp = requests.get('http://localhost/order/list/')
    print(resp.json())
def test_asd11():
    data = {
        # 'user_id': '8370030c-a3ef-4ff3-8c8b-7005e680120a',
        'addr_id': '5f630ecc-ef56-4066-90e3-eed3b01150fe',
        'goods_id':'ffcc0908-cb01-4311-bfaa-651bff372982',
        'goods_cents': 20
    }
    resp = requests.post('http://localhost:8000/order/',json=data)
    # resp = requests.get('http://localhost/order/list/')
    print(resp.json())

if __name__ == '__main__':
    # test_asd()
    test_asd11()