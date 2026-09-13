"""第 1 集：NumPy 和 Pandas 有什么用？"""

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

print("\n选择建议：")
print("NumPy  -> 多维数值数组、矩阵运算、科学计算")
print("Pandas -> 带行列标签的表格、清洗、统计、合并和导入导出")
