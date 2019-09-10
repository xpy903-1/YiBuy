import json

with open('data.json', 'r', encoding='utf-8') as f:
     r = json.load(f)
     for f in r:
         for i in f['Data']['CommodityList']:

             uid = i['CommodityId']
             goods_img = i['SmallPic']
             name = i['CommodityName']
             goods_prcir = i['OriginalPrice']
             sales_volume = i['MaxLimitCount']
             storage = 100
             market_price = i['SellPrice']
             produce_place= '西安'
             detail_img = i['SmallPic']
             description = i['SubTitle']
             detail = i['SubTitle']
             is_selected = i['CanAddToCart']
             print((uid, name, goods_img, goods_prcir, storage, market_price, produce_place, detail_img,
                    detail, is_selected))


