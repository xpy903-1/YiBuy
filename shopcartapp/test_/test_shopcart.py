import random
from unittest import TestCase

import requests

test_data = {

}
class  ShopCartTest(TestCase):
    def test_all_hotgoods(self):
        url = 'http://127.0.0.1:8000/shopcart/hotgood/'
        resp = requests.get(url)
        hotgoods_list = resp.json().get('data')

        hotgoods_random = random.choice(hotgoods_list)
        test_data['goods_price'] = hotgoods_random['goods_price']
        test_data['uid'] = hotgoods_random['uid']
        print('热门商品',
              test_data['uid'],
              hotgoods_random['name'],
              test_data['goods_price'])

    def test_all_is_goodsed(self):
        url = 'http://127.0.0.1:8000/shopcart/isgoods/'
        resp = requests.get(url)
        isgoods_list = resp.json().get('data')

        isgoods_random = random.choice(isgoods_list)
        test_data['goods_price'] = isgoods_random['goods_price']
        print('精选商品',
              isgoods_random['name'],
              test_data['goods_price'])

if __name__ == '__main__':
    ShopCartTest()