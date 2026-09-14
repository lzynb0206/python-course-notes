"""
第 11 集：Pandas 的 Series、DataFrame 和常用概览操作。

Series 是带索引的一维数据；DataFrame 是共享同一行索引的多列数据。与 NumPy
二维数组相比，DataFrame 的每一列可以有自己的名称和 dtype，因此更适合姓名、
日期、金额、类别等现实表格。

拿到一张陌生表时，建议先查看：
1. head/tail：数据长什么样。
2. shape、index、columns：表有多大，行列标签是什么。
3. dtypes：每列是否被解析成正确类型。
4. describe：数值列的大致分布。

Pandas 按标签自动对齐数据。这很强大，但索引不一致时也可能产生 NaN。
"""

import numpy as np
import pandas as pd


print("1. Series：一维数据 + 索引")
series = pd.Series([1, 3, 6, np.nan, 4, 1], name="value")
print(series)
print("值：", series.to_numpy())
print("索引：", series.index)


print("\n2. DataFrame：二维表格 + 行列标签")
dates = pd.date_range("2026-01-01", periods=6)
rng = np.random.default_rng(seed=42)
frame = pd.DataFrame(
    rng.normal(size=(6, 4)).round(2),
    index=dates,
    columns=["A", "B", "C", "D"],
)
print(frame)


print("\n3. 不同列可以使用不同 dtype")
mixed = pd.DataFrame(
    {
        "count": pd.Series([1, 2, 3], dtype="int64"),
        "price": pd.Series([9.9, 12.5, 8.0], dtype="float64"),
        "category": pd.Categorical(["A", "B", "A"]),
        "available": [True, False, True],
    }
)
print(mixed)
print("\ndtypes：\n", mixed.dtypes)


print("\n4. 查看表格结构")
print("index：", frame.index)
print("columns：", frame.columns.to_list())
print("shape：", frame.shape)
print("前 3 行：\n", frame.head(3))
print("后 2 行：\n", frame.tail(2))
print("数值统计：\n", frame.describe().round(2))


print("\n5. 转置和排序")
print("转置后的 shape：", frame.T.shape)
print("列名降序：\n", frame.sort_index(axis=1, ascending=False).head(2))
print("按 B 列升序：\n", frame.sort_values(by="B").head(3))

# Series 类似“带索引的一维数组”；DataFrame 类似“多列对齐的 Series”。
# NumPy 更关注位置与形状，Pandas 还会按照索引和列名自动对齐数据。
