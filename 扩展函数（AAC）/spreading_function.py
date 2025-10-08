import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import io
import base64
from IPython.display import display, Image

# 使用 Agg 后端，这样就不需要图形用户界面
matplotlib.use('Agg')


def spreading_function(i, j):
    """
    根据图片中的公式计算扩展函数 sprdngf(i, j) 的值。

    参数:
    i (float or array-like): 信号的巴克值 (Bark value)
    j (float or array-like): 被扩散到的频带的巴克值

    返回:
    float or array-like: 扩展函数的值
    """
    # 计算临时变量 tmpx
    # 使用 np.where 来处理 j >= i 和 j < i 的情况，方便向量化计算
    tmpx = np.where(j >= i, 3.0 * (j - i), 1.5 * (j - i))

    # 计算临时变量 tmpz
    # minimum(a, b) 返回 a 和 b 中更小（更负）的值
    tmpz_val = (tmpx - 0.5)**2 - 2 * (tmpx - 0.5)
    tmpz = 8 * np.minimum(tmpz_val, 0)

    # 计算临时变量 tmpy
    tmpy = 15.811389 + 7.5 * (tmpx + 0.474) - 17.5 * np.sqrt(1.0 + (tmpx + 0.474)**2)

    # 计算最终的 sprdngf(i, j)
    # 10^((tmpz + tmpy)/10)
    sprdngf = np.where(tmpy < -100, 0, 10**((tmpz + tmpy) / 10.0))

    return sprdngf

# --- 绘图部分 ---

# 设定一个固定的信号巴克值 i
i_fixed = 10.0

# 创建一个围绕 i_fixed 的 j 值数组
# 我们关心的是 j 和 i 的相对差异，所以我们以 (j - i) 作为横坐标
j_minus_i = np.linspace(-8, 5, 200)
j_values = i_fixed + j_minus_i

# 计算对应的扩展函数值
sprdngf_values = spreading_function(i_fixed, j_values)

# 创建图像
plt.figure(figsize=(10, 6))
plt.plot(j_minus_i, sprdngf_values, label=f'Spreading from i = {i_fixed}')

# 设置图像标题和坐标轴标签
plt.title("Psychoacoustic Spreading Function", fontsize=16)
plt.xlabel("Bark Value Difference (j - i)", fontsize=12)
plt.ylabel("Spreading Function Value (linear scale)", fontsize=12)
plt.grid(True)
plt.legend()
plt.axvline(x=0, color='r', linestyle='--', linewidth=0.8, label='Signal Frequency (j=i)')
plt.legend()

# 将图像保存到内存中，而不是文件
buf = io.BytesIO()
plt.savefig(buf, format='png')
buf.seek(0)

plt.savefig("spreading_function.png")
print("已保存图像为 spreading_function.png")
# 关闭图像以释放内存
plt.close()

# 将图像数据编码为 Base64 字符串
# image_base64 = base64.b64encode(buf.read()).decode('utf-8')

# 为了显示，我们将直接输出图像
# 在实际环境中，您可能会使用 image_base64
# print(f"data:image/png;base64,{image_base64}")
# 在当前环境中，直接显示图片
from IPython.display import Image
img = Image(buf.read())
display(img)


