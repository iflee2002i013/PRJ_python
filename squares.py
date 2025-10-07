squares = []
for value in range(1, 11):
    square =  value ** 2
    #squares.append(square)
    squares.append(value ** 2)
print(squares)

# 使用列表推导式，可以更加简洁地生成列表squares：
squares = [value **2 for value in range (1,11)]
print(squares)