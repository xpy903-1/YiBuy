
import requests


def test01():
    resp = requests.get('http://127.0.0.1:8000/index/index/')
    print(resp.json())


def test02():
    resp = requests.get('http://127.0.0.1:8000/index/nav/')
    print(resp.json())


def test03():
    resp = requests.get('http://127.0.0.1:8000/index/eat/')
    print(resp.json())


def test04():
    resp = requests.get('http://127.0.0.1:8000/index/card/')
    print(resp.json())


def test05():
    resp = requests.get('http://127.0.0.1:8000/index/welfare/')
    print(resp.json())


if __name__ == '__main__':
    # 首页
    test01()
    # 导航类列表详情
    test02()
    # 吃饭吧详情
    test03()
    # 会员展示页面
    test04()
    # 首页福利页面
    test05()