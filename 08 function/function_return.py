def build_person(first_name, last_name):
    '''返回一个字典，其中包含有关一个人的信息'''
    person = {'first':first_name,'last':last_name}
    return person

musician = build_person('jimi','hendrix')
print(musician)

def get_formmated_name(first_name,last_name):
    """返回规范格式的姓名"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()
'''
while True:
    print("\nPlease tell me your name:")
    f_name = input("First_name:")
    l_name = input('Last name:')

    formatted_name = get_formmated_name(f_name,l_name)
    print(f'\nHello,{formatted_name}!')
'''
# 使用实参列表
def make_pizza(*toppings):
    print(toppings)

make_pizza('mushrooms')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# 使用 ** 运算符传递字典作为实参
def build_profile(first,last, **user_info):
    """创建一个字典，其中包含有关用户的信息"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert','einstein',locaton='princeton',field='physics')
print(user_profile)