"""第 7 集：NumPy 的索引、切片、条件筛选和迭代。"""

import numpy as np


print("一维数组索引：")
one_dimensional = np.arange(3, 15)
print(one_dimensional)
print("下标 3：", one_dimensional[3])
print("最后一项：", one_dimensional[-1])
print("下标 2～5：", one_dimensional[2:6])  # 左闭右开
print("每隔两项：", one_dimensional[::2])


print("\n二维数组索引：")
matrix = np.arange(3, 15).reshape(3, 4)
print(matrix)
print("第 3 行：", matrix[2])
print("第 2 行第 2 列：", matrix[1, 1])
print("第 2 行的第 2～3 列：", matrix[1, 1:3])
print("所有行的第 2 列：", matrix[:, 1])
print("前两行、后两列：\n", matrix[:2, 2:])


print("\n布尔索引：")
mask = matrix > 8
print("条件矩阵：\n", mask)
print("所有大于 8 的值：", matrix[mask])

# 条件可以组合，但每个条件都要加括号；使用 &、|，不要写 and、or。
selected = matrix[(matrix >= 6) & (matrix <= 11)]
print("6～11：", selected)


print("\n整数数组索引（花式索引）：")
print("按指定顺序取第 3、1 行：\n", matrix[[2, 0]])
print("取坐标 (0,1)、(2,3)：", matrix[[0, 2], [1, 3]])


print("\n迭代方式：")
for row in matrix:
    print("一行：", row)

for column in matrix.T:
    print("一列：", column)

print("扁平迭代：", list(matrix.flat))

# ravel 通常尽量返回视图；flatten 总是返回副本。
print("ravel：", matrix.ravel())
print("flatten：", matrix.flatten())

# 重要：基础切片通常是视图，修改切片可能影响原数组；
# 花式索引和布尔索引通常产生副本。第 10 集会专门比较。
