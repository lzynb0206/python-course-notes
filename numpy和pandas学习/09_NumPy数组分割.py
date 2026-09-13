"""第 9 集：NumPy 数组的等分和不等分。"""

import numpy as np


array = np.arange(12).reshape(3, 4)
print("原数组：\n", array)


print("\n按列方向切成 2 份：")
for part in np.split(array, 2, axis=1):
    print(part, "shape=", part.shape)

print("\n按行方向切成 3 份：")
for part in np.split(array, 3, axis=0):
    print(part, "shape=", part.shape)

# np.split 要求能等分，否则抛出 ValueError。
try:
    np.split(array, 3, axis=1)             # 4 列不能等分成 3 份
except ValueError as error:
    print("\n等分失败：", error)


print("\narray_split 允许不等分：")
uneven_parts = np.array_split(array, 3, axis=1)
for part in uneven_parts:
    print(part, "shape=", part.shape)


print("\n按指定边界分割：")
# [1, 3] 表示在列下标 1 和 3 之前切开，得到 [:1]、[1:3]、[3:]。
for part in np.split(array, [1, 3], axis=1):
    print(part)


print("\n便捷函数：")
top, middle, bottom = np.vsplit(array, 3)
left, right = np.hsplit(array, 2)
print("vsplit 的中间一行：\n", middle)
print("hsplit 的右半部分：\n", right)

# vsplit 沿 axis=0 分割，hsplit 沿 axis=1 分割。
# 选择 split 还是 array_split，关键看能否整除以及是否允许各块大小不同。
