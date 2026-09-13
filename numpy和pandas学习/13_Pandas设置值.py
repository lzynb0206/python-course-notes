"""第 13 集：安全地修改单元格、区域和整列数据。"""

import numpy as np
import pandas as pd


dates = pd.date_range("2026-01-01", periods=6)
frame = pd.DataFrame(
    np.arange(24).reshape(6, 4),
    index=dates,
    columns=["A", "B", "C", "D"],
)
print("原表：\n", frame)


print("\n1. 按位置和标签修改单个值")
frame.iloc[2, 2] = 1111
frame.loc["2026-01-03", "D"] = 2222
frame.iat[0, 0] = 100                 # iat：按位置快速访问单值
frame.at[dates[1], "B"] = 200        # at：按标签快速访问单值
print(frame)


print("\n2. 根据条件批量设置")
# 推荐把条件放进 loc，明确指出“修改哪些行的哪一列”。
frame.loc[frame["A"] > 12, "A"] = 0
print(frame)

# 不推荐 frame["A"][frame["A"] > 0] = 0 这样的链式赋值。
# 中间步骤可能是原表的视图，也可能是副本，行为不够明确，并可能出现警告。


print("\n3. 新增标量列")
frame["status"] = "待检查"           # 标量会广播到每一行
print(frame[["A", "status"]])


print("\n4. 新增 Series：Pandas 会按索引对齐")
scores = pd.Series(
    [60, 70, 80],
    index=pd.to_datetime(["2026-01-01", "2026-01-03", "2026-01-06"]),
)
frame["score"] = scores
print(frame[["A", "score"]])

# 只有索引相同的行会获得值，其余行成为 NaN。这是 Pandas 的标签对齐，不是报错。


print("\n5. assign：返回增加了新列的新表")
result = frame.assign(
    total=lambda table: table[["A", "B", "C", "D"]].sum(axis=1),
    passed=lambda table: table["score"].ge(60),
)
print(result[["total", "score", "passed"]])
print("原表是否有 total 列：", "total" in frame.columns)


print("\n6. 删除列")
without_status = frame.drop(columns=["status"])
print(without_status.columns.to_list())

# frame.drop(..., inplace=True) 会直接修改原对象；
# 默认返回新表更容易追踪数据流，复杂处理链中通常也更清楚。
