import random
from unittest import TestCase

import requests

test_data = {

}
class  ShopCart_hot(TestCase):
    def test_all_hotgoods(self):
        url = 'http://127.0.0.1:8000/shopcart/hotgood/'
        resp = requests.get(url)
        hotgoods_list = resp.json().get('data')

        hotgoods_random = random.choice(hotgoods_list)
        test_data['goods_price'] = hotgoods_random['goods_price']
        print('热门商品',
              hotgoods_random['name'],
              test_data['goods_price'])
