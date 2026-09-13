"""第 6 集：NumPy 基础运算二——统计、轴、转置和累计运算。"""

import numpy as np


array = np.arange(2, 14).reshape(3, 4)
print("原数组：\n", array)

print("\n整体统计：")
print("最小值及扁平索引：", array.min(), array.argmin())
print("最大值及扁平索引：", array.max(), array.argmax())
print("总和：", array.sum())
print("平均值：", array.mean())
print("中位数：", np.median(array))
print("标准差：", array.std().round(3))

# axis 指定“压缩掉哪一个轴”。
# 对 shape=(3, 4) 的二维数组：
# axis=0 压缩行，得到每一列的结果，形状为 (4,)
# axis=1 压缩列，得到每一行的结果，形状为 (3,)
print("\n按列求和 axis=0：", array.sum(axis=0))
print("按行求和 axis=1：", array.sum(axis=1))
print("每列最大值索引：", array.argmax(axis=0))

# keepdims=True 会保留被压缩的维度，便于后续广播。
row_means = array.mean(axis=1, keepdims=True)
centered = array - row_means
print("\n每行均值：\n", row_means)
print("每行中心化：\n", centered)

print("\n累计与相邻差：")
print("cumsum：", np.cumsum(array))
print("每行 cumsum：\n", np.cumsum(array, axis=1))
print("每行 diff：\n", np.diff(array, axis=1))

print("\n查找满足条件的位置：")
rows, columns = np.where(array > 8)
print("行索引：", rows)
print("列索引：", columns)
print("对应值：", array[rows, columns])

print("\n转置与裁剪：")
print("array.T 的形状：", array.T.shape)
print(array.T)
print("clip 到 [5, 10]：\n", np.clip(array, 5, 10))
