# for循环打印1~20
for i in range(1,21):
    print(i)

# 创建一个1~100万的列表
list_100w = []
for i in range(1,1000001):
    list_100w.append(i)

print(min(list_100w))
print(max(list_100w))
print(sum(list_100w))

# 通过range()函数创建列表,1~20的奇数
list_odd = list(range(1,21,2))
for odd in list_odd:
    print(odd)

# 创建一个列表,其中包含 3~30 内能被 3 整除的数
list_3div = []
for i in range(3,31):
    if i % 3 == 0:
        list_3div.append(i)
print(list_3div)

list_3 = list(range(3,31,3))
for num in list_3:
    print(num)

# 创建一个列表，其中包含前10个整数（1~10）的立方
list_cube = []
for num in range(1,11):
    cube = num ** 3
    list_cube.append(cube)
print(list_cube)

list_cube = [num ** 3 for num in range(1,11)]
print(list_cube)

# 