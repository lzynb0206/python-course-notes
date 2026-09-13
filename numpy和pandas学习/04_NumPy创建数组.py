"""第 4 集：用不同方式创建 NumPy 数组。"""

import numpy as np


def show(title, value):
    print(f"\n{title}\n{value}")


# 1. 从 Python 列表或元组创建。
show("一维数组", np.array([2, 23, 4]))
show("二维数组", np.array([[2, 23, 4], [5, 6, 7]]))

# 2. dtype 决定元素的表示方式和占用空间。
integers = np.array([2, 23, 4], dtype=np.int32)
floats = np.array([2, 23, 4], dtype=np.float64)
print("\n整数 dtype：", integers.dtype)
print("浮点 dtype：", floats.dtype)

# 3. 创建指定形状的数组。
show("全 0", np.zeros((2, 3)))
show("全 1", np.ones((2, 3), dtype=np.int64))
show("填满指定值", np.full((2, 3), 7))
show("单位矩阵", np.eye(3, dtype=np.int64))

# empty 只分配内存，不保证初始值为 0。使用前必须把内容完整写入。
empty_array = np.empty((2, 2))
print("\nempty 的形状：", empty_array.shape)

# 4. arange 类似 range，但可以生成 NumPy 数组并支持浮点步长。
show("arange(2, 10, 2)", np.arange(2, 10, 2))

# 5. linspace 更关心“生成几个等间隔点”，默认包含终点。
show("0 到 1 之间的 5 个点", np.linspace(0, 1, 5))

# arange 适合明确步长；linspace 适合明确点的数量。
print("\narange 与 linspace：")
print("np.arange(0, 1, 0.25) ->", np.arange(0, 1, 0.25))
print("np.linspace(0, 1, 5)  ->", np.linspace(0, 1, 5))

# 6. 使用新版随机数生成器，传入种子可得到可复现结果。
rng = np.random.default_rng(seed=42)
show("0～9 的随机整数", rng.integers(0, 10, size=(2, 3)))
show("标准正态分布随机数", rng.normal(size=(2, 3)).round(3))

# 7. astype 创建转换 dtype 后的新数组。
text_numbers = np.array(["1", "2", "3"])
converted = text_numbers.astype(np.int64)
print("\n转换前：", text_numbers, text_numbers.dtype)
print("转换后：", converted, converted.dtype)
