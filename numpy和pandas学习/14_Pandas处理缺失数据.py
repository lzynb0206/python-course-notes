"""
第 14 集：识别、删除、填充和统计缺失数据。

缺失值表示“这条信息没有记录”，不等于数字 0，也不等于空字符串。处理步骤通常
是先统计缺失位置和比例，再结合字段含义决定删除、填充还是保留。

常用方法：
- isna/notna：识别缺失或非缺失位置。
- dropna：删除不满足完整性要求的行或列。
- fillna：使用固定值、均值、中位数等填充。
- ffill/bfill：使用前一条或后一条有效记录填充。
- interpolate：按相邻数值的变化趋势插值。

不存在适合所有数据的填充规则。比如缺失成绩填 0 会把“没参加考试”误解释成
“参加了但得零分”，因此清洗前必须先理解业务含义。
"""

import numpy as np
import pandas as pd


frame = pd.DataFrame(
    {
        "name": ["小明", "小红", "小刚", "小兰"],
        "math": [88.0, np.nan, 76.0, 92.0],
        "english": [90.0, 95.0, np.nan, 89.0],
        "city": ["北京", None, "上海", "北京"],
    }
)
print("原表：\n", frame)


print("\n1. 识别缺失值")
print(frame.isna())
print("每列缺失数量：\n", frame.isna().sum())
print("每列非缺失数量：\n", frame.notna().sum())


print("\n2. dropna 删除缺失数据")
print("只要该行有缺失就删除：\n", frame.dropna())
print("只检查成绩列：\n", frame.dropna(subset=["math", "english"]))
print("至少保留 3 个非缺失值：\n", frame.dropna(thresh=3))

# axis=0 删除行（默认），axis=1 删除列。
# how="any" 表示出现任意缺失就删除，how="all" 表示全部缺失才删除。


print("\n3. fillna 填充缺失数据")
filled = frame.fillna(
    {
        "math": frame["math"].mean(),
        "english": frame["english"].median(),
        "city": "未知",
    }
)
print(filled.round(2))


print("\n4. 前向填充和插值")
time_series = pd.Series([10.0, np.nan, np.nan, 16.0, 20.0])
print("原序列：", time_series.to_list())
print("前向填充：", time_series.ffill().to_list())
print("后向填充：", time_series.bfill().to_list())
print("线性插值：", time_series.interpolate().to_list())


print("\n5. 修改原表还是返回新表")
copy = frame.copy()
copy["city"] = copy["city"].fillna("未知")
print(copy)

# 缺失值不能随意统一填成 0：
# 0 可能表示真实的“成绩为零”，而 NaN 表示“没有记录”。填充策略要结合业务含义。
