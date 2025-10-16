import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8-darkgrid')

fig, ax = plt.subplots()

ax.scatter(2, 4, s=200)

# 设置图表标题和标签
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# 设计刻度标记
ax.tick_params(labelsize=14)

plt.show()