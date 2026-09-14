"""
第 1 集：NumPy 和 Pandas 有什么用？

学习目标：
1. 理解 Python 列表和 NumPy 数组的定位差异。
2. 理解“向量化”为什么能让数值代码更简洁。
3. 知道 Series、DataFrame 分别表示什么。

核心理解：
- NumPy 擅长处理形状规则、元素类型一致的多维数值数据。
- Pandas 在数组之上增加了行列标签，适合处理现实中的表格数据。
- 两者不是互相替代：实际分析中经常用 Pandas 整理数据，再用 NumPy 计算。

下面的 print 只用来观察运算结果；概念解释都写在代码注释中。
"""

import numpy as np
import pandas as pd


def show_title(title):
    print(f"\n{'=' * 10} {title} {'=' * 10}")


show_title("1. NumPy：高效处理同类型数值")

# Python 列表可以存放不同类型的数据，使用灵活。
python_list = [10, 20, 30, 40]

# ndarray 通常保存同一种 dtype，数据排列紧凑，适合批量数值计算。
numpy_array = np.array(python_list)
print("Python 列表：", python_list)
print("NumPy 数组：", numpy_array)

# 列表乘 2 是重复内容；数组乘 2 是每个元素分别乘 2。
print("列表 * 2：", python_list * 2)
print("数组 * 2：", numpy_array * 2)

# NumPy 的核心思路是“向量化”：把整组数据交给底层实现一次处理，
# 不需要自己写 Python for 循环逐个计算。
temperatures = np.array([18.5, 20.0, 21.5, 19.0])
fahrenheit = temperatures * 9 / 5 + 32
print("摄氏温度：", temperatures)
print("华氏温度：", fahrenheit)


show_title("2. Pandas：带标签的表格数据")

# DataFrame 可以看作一张二维表：列有名称，行也有索引。
# 不同列可以保存不同类型，这是它和普通二维 ndarray 的重要区别。
students = pd.DataFrame(
    {
        "name": ["小明", "小红", "小刚"],
        "score": [88, 95, 76],
        "passed": [True, True, True],
    }
)
print(students)

# 选择一列、按条件筛选、统计平均值都可以直接表达。
print("\n成绩列：")
print(students["score"])
print("\n90 分及以上：")
print(students.loc[students["score"] >= 90, ["name", "score"]])
print("\n平均分：", students["score"].mean())


show_title("3. 两者如何配合")

# Pandas 的很多数值能力建立在 NumPy 之上。
# 常见流程：Pandas 读取并整理表格 -> NumPy 做数值计算 -> Pandas 展示结果。
students["standard_score"] = (
    students["score"] - students["score"].mean()
) / students["score"].std(ddof=0)
print(students.round(2))

# 选择建议：
# - 面对规则的多维数值、矩阵运算或科学计算，先想到 NumPy。
# - 面对带字段名的表格、缺失值、分组、合并或文件导入，先想到 Pandas。
