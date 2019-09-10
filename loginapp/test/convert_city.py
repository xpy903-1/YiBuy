import json

with open('city.json', 'r', encoding='utf-8') as f:
    city_dict = json.load(f)
    for i in city_dict['Data']['CityList']:
        for r in i['CityList']:
            name = r['AreaName']
            start_str = r['FirstLetter']
            print(name, start_str)