from unittest import TestCase, TestSuite, TextTestRunner
import requests

class TestGoodsModel(TestCase):
    def test_01_query_info(self):
        url = 'http://localhost:8000/goods/detail/fff7f38e-d3db-48db-9db0-b515d7a5776f'
        resp = requests.get(url)
        print(resp.json())

    def test_02_query_img(self):
        url = 'http://localhost:8000/goods/queryimg/img/fff7f38e-d3db-48db-9db0-b515d7a5776f'
        resp = requests.get(url)
        print(resp.json())

    def test_03_goodsclassify(self):
        url = 'http://localhost:8000/goods/type/list/'
        resp = requests.get(url)
        print(resp.json())

    def test_04_search(self):
        url = 'http://localhost:8000/goods/search/?word=苹果'
        resp = requests.get(url)
        print(resp.json())

if __name__ == '__main__':
    suite1 = TestSuite()
    suite1.addTest(TestGoodsModel.test_01_query_info)

    suite2 = TestSuite()
    suite2.addTest(TestGoodsModel.test_02_query_img)

    suite3 = TestSuite()
    suite3.addTest(TestGoodsModel.test_03_goodsclassify)

    suite4 = TestSuite()
    suite4.addTest(TestGoodsModel.test_04_search)

    TextTestRunner().run(TestSuite(suite1(), suite2(), suite3(), suite4()))


