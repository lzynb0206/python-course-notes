"""第 5 集：NumPy 基础运算一——逐元素运算、比较和矩阵乘法。"""

import numpy as np


a = np.array([10, 20, 30, 40])
b = np.arange(4)

print("a：", a)
print("b：", b)
print("a + b：", a + b)
print("a - b：", a - b)
print("a * b：", a * b)       # 对应位置相乘，不是矩阵乘法
print("a / (b + 1)：", a / (b + 1))
print("b ** 2：", b**2)
print("b < 3：", b < 3)

# NumPy 通用函数会逐元素计算。
angles = np.array([0, np.pi / 2, np.pi])
print("\nsin：", np.sin(angles).round(6))
print("sqrt：", np.sqrt(np.array([1, 4, 9])))
print("exp：", np.exp(np.array([0, 1])).round(3))


print("\n逐元素乘法与矩阵乘法：")
left = np.array([[1, 2], [3, 4]])
right = np.array([[5, 6], [7, 8]])
print("left * right：\n", left * right)
print("left @ right：\n", left @ right)
print("np.dot(left, right)：\n", np.dot(left, right))

# 对二维数组，@ 的规则是：(m, n) @ (n, p) -> (m, p)。
print("参与矩阵乘法的形状：", left.shape, right.shape)


print("\n广播：不同形状也可能参与逐元素运算")
matrix = np.arange(12).reshape(3, 4)
row_offsets = np.array([10, 20, 30, 40])
column_offsets = np.array([[100], [200], [300]])
print("原矩阵：\n", matrix)
print("每列加一个值：\n", matrix + row_offsets)
print("每行加一个值：\n", matrix + column_offsets)

# 广播从最后一个维度向前比较：维度长度相同或其中一个为 1 才兼容。
# (3, 4) + (4,)    -> (3, 4)
# (3, 4) + (3, 1)  -> (3, 4)
