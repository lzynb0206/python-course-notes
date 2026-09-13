"""第 8 集：NumPy 数组的纵向、横向及指定轴合并。"""

import numpy as np


a = np.array([1, 1, 1])
b = np.array([2, 2, 2])
print("a.shape：", a.shape)              # (3,)，一维数组没有行列之分


print("\n一维数组直接合并：")
vertical = np.vstack((a, b))
horizontal = np.hstack((a, b))
print("vstack：\n", vertical)
print("vstack.shape：", vertical.shape)   # (2, 3)
print("hstack：", horizontal)
print("hstack.shape：", horizontal.shape) # (6,)


print("\n用 newaxis 增加维度：")
row = a[np.newaxis, :]                    # (1, 3)，一行
column = a[:, np.newaxis]                 # (3, 1)，一列
print("行向量：\n", row, row.shape)
print("列向量：\n", column, column.shape)

# None 与 np.newaxis 作用相同。
print("a[:, None].shape：", a[:, None].shape)


print("\n二维数组合并：")
left = np.array([[1, 2], [3, 4]])
right = np.array([[5, 6], [7, 8]])
print("axis=0，增加行：\n", np.concatenate((left, right), axis=0))
print("axis=1，增加列：\n", np.concatenate((left, right), axis=1))

# vstack 基本对应 concatenate(..., axis=0)
# hstack 对二维数组基本对应 concatenate(..., axis=1)
print("vstack：\n", np.vstack((left, right)))
print("hstack：\n", np.hstack((left, right)))


print("\nstack 会创建一个新轴：")
print("axis=0 的 shape：", np.stack((left, right), axis=0).shape)  # (2, 2, 2)
print("axis=1 的 shape：", np.stack((left, right), axis=1).shape)  # (2, 2, 2)

print("\n列合并的便捷写法：")
print(np.column_stack((a, b)))

# 合并前要检查除目标轴以外的形状是否一致。
# 例如按 axis=0 合并二维数组时，列数必须相同。
