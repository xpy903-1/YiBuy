import json


def get_city(citys):
    sub_str = ''
    for city in citys:
        id = city['AreaId']
        # code = city['AreaCode']
        name = city['AreaName']
        start_str = city['FirstLetter']

        sub_str += "('%s', '%s', '%s'),\n" % (id, name, start_str)

    return sub_str


with open('city.json', encoding='utf-8') as f:
    city_dict = json.load(f)
    all_city = city_dict['Data']['CityList']
