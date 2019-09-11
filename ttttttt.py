import json
from goodsapp.models import SecClassify

with open('data.json', 'r', encoding='utf-8') as f:
     r = json.load(f)
     for f in r:
         for i in f['Data']['CommodityList']:

            SecClassify.objects.get(pk='f92e1d5a-b701-4905-a223-d42e93dc926c').goods.create(
                goods_img=i['SmallPic'],
                name=i['CommodityName'],
                goods_price=i['OriginalPrice'],
                sales_volume=i['MaxLimitCount'],
                storage=100,
                market_price=i['SellPrice'],
                produce_place='西安',
                detail_img=i['SmallPic'],
                description=i['SubTitle'],
                detail=i['SubTitle'],
                is_selected=i['CanAddToCart']
            )

print('完成')
