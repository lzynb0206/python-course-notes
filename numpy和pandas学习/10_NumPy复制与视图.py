"""第 10 集：理解赋值、视图（浅层共享）和深拷贝。"""

import numpy as np


def print_relation(name, original, other):
    print(
        f"{name}: 同一对象={other is original}, "
        f"共享内存={np.shares_memory(original, other)}"
    )


print("1. 直接赋值：两个变量指向同一个数组对象")
a = np.arange(4)
b = a
print_relation("b = a", a, b)
b[0] = 100
print("修改 b 后 a：", a)


print("\n2. view：对象不同，但底层数据共享")
a = np.arange(6)
view = a.view()
print_relation("a.view()", a, view)
view[1] = 200
print("修改 view 后 a：", a)


print("\n3. 基础切片通常也是视图")
a = np.arange(8)
slice_view = a[2:6]
print_relation("a[2:6]", a, slice_view)
slice_view[:] = -1
print("修改切片后 a：", a)


print("\n4. copy：对象和数据都独立")
a = np.arange(4)
deep_copy = a.copy()
print_relation("a.copy()", a, deep_copy)
deep_copy[0] = 999
print("原数组：", a)
print("副本：", deep_copy)


print("\n5. 花式索引通常返回副本")
a = np.arange(6)
fancy_copy = a[[0, 2, 4]]
print_relation("a[[0, 2, 4]]", a, fancy_copy)
fancy_copy[0] = 500
print("修改花式索引结果后 a：", a)


print("\n选择建议：")
print("只想给同一个数组增加别名       -> b = a")
print("想换一种形状观察并共享原数据   -> view 或基础切片")
print("希望后续修改完全互不影响       -> a.copy()")

# 为什么要在意共享内存？
# 好处：避免复制大数组，节省时间和内存。
# 风险：修改视图会悄悄改变原数组。函数要修改输入前，先明确是否应该 copy。
