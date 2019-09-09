import json

def get_category(categorys):
    sub_str = ""
    for category in categorys:
        id = category['CategoryId']
        code = category['CategoryCode']
        name = category['CategoryName']
        grade = category['Grade']
        picture_url = category['PictureUrl']
        parent_id = category['PriorId']
        if name == '全部':
            continue
        sub_str += "('%s', '%s', '%s', %s, '%s', '%s'),\n" % (id,name,code,grade,picture_url,parent_id)

        if category['Childs']:
            sub_str += get_category(category['Childs'])

    return sub_str

with open('category.json', 'r', encoding='UTF-8') as f:
    category_dict = json.load(f)
    all_category = category_dict['Data']['CategoryList']

    sql = 'INSERT INTO t_category(id,code,name,grade,picture_url,parent_id) VALUES '

    sub_str = get_category(all_category)

    with open('category.sql', 'w', encoding='UTF-8') as sql_f:
        sql_f.write(sql+'\n'+sub_str)


