import json



with open('city.json', encoding='utf-8') as f:
    city_dict = json.load(f)
    all_city = city_dict['Data']['CityList']
