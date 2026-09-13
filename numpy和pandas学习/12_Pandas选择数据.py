"""第 12 集：用列名、loc、iloc 和布尔条件选择 Pandas 数据。"""

import numpy as np
import pandas as pd


dates = pd.date_range("2026-01-01", periods=6)
frame = pd.DataFrame(
    np.arange(24).reshape(6, 4),
    index=dates,
    columns=["A", "B", "C", "D"],
)
print("原表：\n", frame)


print("\n1. 选择列")
print("单列返回 Series：\n", frame["A"])
print("多列返回 DataFrame：\n", frame[["A", "C"]])


print("\n2. loc：按标签选择")
print("某一天：\n", frame.loc["2026-01-02"])
print("全部行的 A、B 列：\n", frame.loc[:, ["A", "B"]])
print("某个单元格：", frame.loc["2026-01-02", "B"])
print("标签切片包含结束标签：\n", frame.loc["2026-01-02":"2026-01-04", "B":"C"])


print("\n3. iloc：按整数位置选择")
print("第 4 行：\n", frame.iloc[3])
print("第 4 行第 2 列：", frame.iloc[3, 1])
print("第 4～5 行、前两列：\n", frame.iloc[3:5, 0:2])
print("指定行列位置：\n", frame.iloc[[1, 2, 4], [0, 2]])

# iloc 与普通 Python 切片一样，不包含结束位置。


print("\n4. 布尔筛选")
print("A 列大于 8 的行：\n", frame.loc[frame["A"] > 8])
print("A > 8 且 D < 20：\n", frame.loc[(frame["A"] > 8) & (frame["D"] < 20)])
print("满足条件的行，只看 A、D：\n", frame.loc[frame["A"] >= 12, ["A", "D"]])


print("\n5. query 与单值访问")
print(frame.query("A >= 8 and D <= 19"))
print("at 按标签取单值：", frame.at[dates[0], "A"])
print("iat 按位置取单值：", frame.iat[0, 0])

print("\nloc 与 iloc 速记：")
print("loc  -> label，使用真实标签；标签切片包含终点")
print("iloc -> integer location，使用整数位置；位置切片不包含终点")

# 原课程中的 ix 已被 Pandas 移除。现在应明确选择 loc 或 iloc，
# 这样代码含义更清楚，也不会依赖模糊的“标签或位置混合判断”。
