import matplotlib.pyplot as plt
print(plt.style.available)

# 设置输入值和平方值
input_values = [1,2,3,4,5]
squares = [1,4,9,16,25]

# 可以给图表添加样式
plt.style.use('seaborn-v0_8-darkgrid')

# 创建图表
# 这个fig ax 的写法是固定的 fig表示整个图表，ax表示图表中的一个子图
# 如果只有一个子图，可以直接用fig, ax = plt.subplots()，如果有多个子图，可以用fig, (ax1, ax2) = plt.subplots(1, 2)表示一行两列的两个子图
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

# 设置图表标题和标签
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# 设计刻度标记
ax.tick_params(labelsize=14)

# 显示图表
plt.show()