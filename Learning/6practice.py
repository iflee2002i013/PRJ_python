# 创建表示宠物的字典
pet_1 = {'type': 'dog', 'owner': 'Alice'}
pet_2 = {'type': 'cat', 'owner': 'Bob'}
pet_3 = {'type': 'fish', 'owner': 'Charlie'}
pet_4 = {'type': 'parrot', 'owner': 'David'}

# 将字典存储在一个列表中
pets = [pet_1, pet_2, pet_3, pet_4]

# 遍历列表并打印每个宠物的信息
for pet in pets:
    pet_type = pet['type']
    owner_name = pet['owner']
    print(f"Pet Type: {pet_type.title()}, Owner: {owner_name.title()}")

print('\n')
# 第二个练习
favorite_places = {
    'Alice':['New York','Wu Han','Paris'],
    'Bob':['Tokyo','Osaka','Kyoto'],
    'Charile':['Beijing','Shanghai','Guangzhou']
}

for name,places in favorite_places.items():
    print(f"{name}'s favourite places is ")
    for place in places:
        print(f"- {place}")


# 第三个练习
cities = {
    'New York': {'country':'US',
                 'population':'834W',
                 'fact':'The area is 1214'
    },
    'Tokyo':{'country':'Japan',
             'population':'1.3B',
             'fact':'The area is 377,972',
    },
    'HanDan':{'country':'China',
                 'population':'1.2B',
                 'fact':'The area is 361,742',
    }
}

for city,info in cities.items():
    print(f"\nCity:{city}")
    Country = info['country']
    fact = info['fact']
    print(f"\tBelongs to {Country}")
    print(f"\t{fact}")