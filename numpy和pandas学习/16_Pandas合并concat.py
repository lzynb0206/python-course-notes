"""第 16 集：使用 pd.concat 沿行或列拼接数据。"""

import numpy as np
import pandas as pd


columns = ["a", "b", "c", "d"]
frame_0 = pd.DataFrame(np.zeros((3, 4), dtype=int), columns=columns)
frame_1 = pd.DataFrame(np.ones((3, 4), dtype=int), columns=columns)
frame_2 = pd.DataFrame(np.full((3, 4), 2), columns=columns)


print("1. axis=0：纵向追加行")
rows = pd.concat([frame_0, frame_1, frame_2], axis=0, ignore_index=True)
print(rows)

# ignore_index=True 会重新生成 0～n-1 的行索引。
# 如果原索引有业务意义，应保留索引，或者先把它变成普通列。


print("\n2. axis=1：横向增加列")
left = pd.DataFrame(
    np.zeros((3, 3), dtype=int), columns=["a", "b", "c"], index=[1, 2, 3]
)
right = pd.DataFrame(
    np.ones((3, 3), dtype=int), columns=["d", "e", "f"], index=[2, 3, 4]
)

outer = pd.concat([left, right], axis=1, join="outer")
inner = pd.concat([left, right], axis=1, join="inner")
print("outer，保留索引并集：\n", outer)
print("inner，只保留索引交集：\n", inner)


print("\n3. 对齐到指定索引")
# 旧课程中的 join_axes 已经移除，可以先 concat，再用 reindex 明确目标索引。
aligned_to_left = outer.reindex(left.index)
print(aligned_to_left)


print("\n4. 添加一行")
new_row = pd.DataFrame([{"a": 9, "b": 8, "c": 7, "d": 6}])
with_new_row = pd.concat([frame_0, new_row], ignore_index=True)
print(with_new_row)

# DataFrame.append 已从新版 Pandas 移除，统一使用 pd.concat。


print("\n5. keys 创建来源标签")
with_source = pd.concat(
    [frame_0, frame_1],
    keys=["第一组", "第二组"],
    names=["source", "row"],
)
print(with_source)
print("取出第二组：\n", with_source.loc["第二组"])


print("\nconcat 与 merge：")
print("concat -> 按轴堆叠多个对象，主要关心轴和索引如何对齐")
print("merge  -> 根据一列或多列键匹配记录，类似 SQL JOIN")
