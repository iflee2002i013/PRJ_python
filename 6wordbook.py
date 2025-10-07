alien_0 = {'color': 'green','point':5}

print(alien_0['color'])
print(alien_0['point'])

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

#创建一个空字典
alien_0 = {}
# 向字典中添加键值对
alien_0['color'] = 'green'
alien_0['point'] = 5

print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
alien_0['speed'] = 'fast'

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] =='medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position : {alien_0['x_position']}")


# 删除键值对
del alien_0['point']
print(alien_0)

# 使用多行语句创建字典
favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
print(favourite_languages)

point_value = alien_0.get('point', 'No point value assigned')
print(point_value)

# 词汇表
word_book = {}
word_book['apple'] = 'a round fruit with red or green skin and a white flesh'
word_book['banana'] = 'a long curved fruit with yellow skin and a soft inside'
word_book['orange'] = 'a round citrus fruit with orange skin and a soft inside'

print(f"apple: {word_book['apple']}")

print('\n')
# 字典的遍历
user_0 = {'username': 'alice', 'age': 25, 'city': 'New York'}

# 注意key和value的顺序，key就是字典的键，value就是字典的值，虽然可以使用别的变量名，但顺序一定要正确。
# .items()方法可以同时遍历key和value
for key,value in user_0.items():
    print(f"{key}: {value}")

# 遍历字典中的key
# .keys()方法可以遍历字典中的所有key
for name in favourite_languages.keys():
    print(name.title())
# 两者输出一样，因为在遍历字典时，会默认遍历所有key    
for name in favourite_languages:
    print(name.title())

# 字典的嵌套
    alien_0 = {'color':'green','points':5}
    alien_1 = {'color':'yellow','points':10}
    alien_2 = {'color':'red','points':15}

    aliens = [alien_0,alien_1,alien_2] # 将字典放到列表中，但是不能放在字典中

    for alien in aliens:
        print(alien)

# 使用for循环批量创建字典
print('\n')
aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5,'speed': 'fast'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)

print("...")
print(f"Total number of aliens: {len(aliens)}")

# 在字典中存储列表
pizza = {
    'crust': 'thick',
    'toppings':['mushrooms','extra cheese']
}
# 概述顾客点的披萨
print(f"You ordered a {pizza['crust']}-curst pizza"
      " with the following toppings:")
for topping in pizza['toppings']:
    print(f"\t  - {topping}")

# 在字典中存储字典
users = {
    'aeinstein':{
        'first':'albert',
        'last':'einstein',
        'location':'pricenton'
    },
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris'
    }
}
for username,userinfo in users.items():
    print(f"\nUsername:{username}")
    full_name = f"{userinfo['first']} {userinfo['last']}"
    location = userinfo['location']
    print(f"\tFull name: {full_name.title()}")

    print(f"\tFull name {full_name.title()}")
    print(f"\tLocation:{location.title()}")
