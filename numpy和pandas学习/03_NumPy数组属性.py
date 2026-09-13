"""第 3 集：NumPy 数组的常用属性。"""

import numpy as np


array = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.int64)
print("数组：\n", array)

# ndim：维度数量。这里有行和列两个轴，所以是二维。
print("ndim（维度数）：", array.ndim)       # 2

# shape：每个维度的长度。二维数组通常读作 (行数, 列数)。
print("shape（形状）：", array.shape)       # (2, 3)

# size：所有维度合起来的元素总数，等于 2 * 3。
print("size（元素数）：", array.size)        # 6

# dtype：所有元素共享的数据类型。
print("dtype（元素类型）：", array.dtype)    # int64

# itemsize：单个元素占用的字节数；nbytes：数组数据区的总字节数。
print("itemsize（每项字节）：", array.itemsize)
print("nbytes（数据总字节）：", array.nbytes)
print("size * itemsize：", array.size * array.itemsize)


print("\n一维、二维和三维对比：")
one_dimensional = np.array([1, 2, 3])
two_dimensional = np.array([[1, 2, 3]])
three_dimensional = np.array([[[1, 2, 3]], [[4, 5, 6]]])

for name, current in (
    ("一维", one_dimensional),
    ("二维", two_dimensional),
    ("三维", three_dimensional),
):
    print(f"{name}: ndim={current.ndim}, shape={current.shape}, size={current.size}")

# 注意：(3,) 是一维数组；(1, 3) 才是 1 行 3 列的二维数组。
print("\n(3,) 与 (1, 3) 是否相同：", one_dimensional.shape == two_dimensional.shape)


print("\nreshape 只改变观察数据的形状，不改变元素总数：")
numbers = np.arange(12)
matrix = numbers.reshape(3, 4)
print(matrix)
print("reshape 前后 size：", numbers.size, matrix.size)

# reshape 的各维长度乘积必须等于原来的 size。
# 使用 -1 可以让 NumPy 自动推断其中一个维度。
print("自动推断为 2 行：\n", numbers.reshape(2, -1))
