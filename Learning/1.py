first_name = "John"
last_name = "Doe"

full_name = f"{first_name} {last_name}"
print(full_name)

cite = 'Albert Einstein once said, “A person who never made a mistake never tried anything new.”'
print(cite)

# 去除文件扩展名
file_name = "example.txt"
file_name_without_ext = file_name.removesuffix(".txt")
print(file_name_without_ext)

# 数值运算
a = 3 * 0.1
print(a)

# 同时给多个变量赋值
x, y, z = 1, 2, 3
print(x, y, z)

# 常量
MAX_CONNECTIONS = 5000
print(MAX_CONNECTIONS)

import this

# 列表
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[-1])
print(bicycles[1:3])

message = f"My first bicycle was a {bicycles[0].title()}."
print(message)

# 修改列表元素
bicycles[0] = 'honda'
print(bicycles)

# 追加元素
bicycles.append('ducati') # 在列表末尾追加元素
print(bicycles)

# 动态创建列表
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

# 插入元素
motorcycles.insert(0, 'ducati') # 在索引0处插入元素
print(motorcycles)

# 删除元素
del motorcycles[0] # 删除索引0处的元素
print(f"{motorcycles}\n")

# 使用pop()方法删除末尾元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# 使用pop(index)方法删除指定索引处的元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop(1)
print(motorcycles)
print(popped_motorcycle) # 输出：'yamaha'

# 使用remove()方法删除指定元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.remove('yamaha')
print(motorcycles) # 输出：['honda','suzuki']

print("\n")
# 使用sort()方法对列表进行排序
cars = ['bmw', 'audi', 'toyota', 'tesla']
print(cars)
cars.sort()
print(cars) # 输出：['audi', 'bmw', 'tesla', 'toyota']
cars.sort(reverse=True)
print(cars) # 输出：['toyota', 'tesla', 'bmw', 'audi']

print("\n")
# 使用sorted()函数对列表进行临时排序
cars = ['bmw', 'audi', 'toyota', 'tesla']
print(cars)
print(sorted(cars))
print(cars)
print(sorted(cars, reverse=True))
print(cars)

# 使用len()函数获取列表长度
cars = ['bmw', 'audi', 'toyota', 'tesla']
print(len(cars)) # 输出：4

print("\n")
# 使用for循环遍历列表元素
magicians = ['alice', 'david', 'carolina']
for magicianm in magicians:
    print(magicianm)

print("\n")
# 使用range()函数生成数字序列
for value in range(1,6):
    print(value)
# 使用list()函数将range()函数生成的序列转换为列表
numbers = list(range(6))
print(numbers)
# 使用range()指定步长
numbers = list(range(1,11,2))
print(numbers)

print("\n")
# 对数值列表执行简单的统计计算
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

# 输出列表中的slice
players = ['charles', 'martina', 'florence', 'eli']
print(players[0:3])
print(players[:3])
print(players[2:])
# 输出最后三个元素
print(players[-3:])

# 复制列表
my_list = [1, 2, 3]
my_list_copy = my_list[:]
print(my_list_copy)

print("\n")
# 定义元组
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

# 修改元组（唯一方式是重新赋值）
# 适用于整个代码块中只读的元组
dimensions = (200,50)
dimensions = (100,100)
print(dimensions)

