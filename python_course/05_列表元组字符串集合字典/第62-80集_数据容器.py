"""
第 62～80 集：列表、元组、字符串、集合、字典与数据容器通用操作。

运行方式：
    python3 第62-80集_数据容器.py

学习目标：
1. 掌握五类数据容器的定义、取值、修改和遍历。
2. 掌握序列切片，以及 len、max、min、sorted 等通用函数。
3. 掌握 list、tuple、str、set 之间的转换并进行横向比较。
4. 理解字符串比较实际上是逐字符比较字符编码。
"""


def show_title(title):
    """打印章节分隔线，让运行结果更容易阅读。"""
    print(f"\n{'=' * 12} {title} {'=' * 12}")


show_title("1. 第 62～64 集：数据容器、列表和下标")

# 数据容器可以一次保存多个数据。列表使用方括号，元素之间用逗号分隔。
names = ["小明", "小红", "小刚"]
mixed_list = ["小明", 18, True]            # 同一列表可以保存不同类型
nested_list = [["小明", 18], ["小红", 19]]

print("列表：", names)
print("正向下标 0：", names[0])            # 小明
print("反向下标 -1：", names[-1])          # 小刚
print("嵌套列表取值：", nested_list[1][0])  # 小红

# 下标从 0 开始；超出范围会产生 IndexError。
try:
    print(names[3])
except IndexError as error:
    print("下标越界：", error)


show_title("2. 第 65～67 集：列表常用操作与遍历")

students = ["小明", "小红", "小刚"]
print("小红的下标：", students.index("小红"))

students[0] = "小明同学"                  # 修改指定下标
students.insert(1, "小李")                # 在指定下标插入
students.append("小王")                   # 末尾追加一个元素
students.extend(["小赵", "小钱"])        # 末尾追加一批元素
print("新增后：", students)

removed_by_pop = students.pop(1)           # 删除指定下标并返回被删除元素
students.remove("小刚")                   # 删除第一个匹配元素
del students[0]                            # 按下标删除
print("pop 删除的元素：", removed_by_pop)
print("删除后：", students)
print("小王出现次数：", students.count("小王"))
print("列表元素数量：", len(students))

print("for 遍历：")
for student in students:
    print(student)

print("while 遍历：")
index = 0
while index < len(students):
    print(index, students[index])
    index += 1


show_title("3. 第 68 集：元组")

# 元组和列表一样有序、支持下标、允许重复，但元组内容不能修改。
person = ("小明", 18, "男")
single_item_tuple = (100,)                 # 单元素元组必须保留逗号
print(person[0])
print(single_item_tuple, type(single_item_tuple))
print("18 的下标：", person.index(18))
print("小明出现次数：", person.count("小明"))

# 元组本身不能修改，但如果元组内放着列表，列表内部仍然可以修改。
special_tuple = ("成绩", [80, 90])
special_tuple[1].append(100)
print(special_tuple)                       # ('成绩', [80, 90, 100])


show_title("4. 第 69～70 集：字符串常用操作")

text = "itheima and itcast"
print("下标 0：", text[0])
print("itheima 的起始下标：", text.index("itheima"))
print("替换：", text.replace("itcast", "Python"))
print("分割：", text.split(" "))
print("统计字母 i：", text.count("i"))
print("字符串长度：", len(text))

spaced_text = "  Python 学习  \n"
print("strip 前：", repr(spaced_text))
print("strip 后：", repr(spaced_text.strip()))

# 字符串不可修改；replace、strip 等方法返回新字符串，原字符串保持不变。
print("原字符串仍是：", text)


show_title("5. 第 71～72 集：序列切片")

# 切片格式：序列[start:stop:step]，包含 start，不包含 stop。
sequence = [0, 1, 2, 3, 4, 5, 6]
print(sequence[1:5])                       # [1, 2, 3, 4]
print(sequence[:4])                        # [0, 1, 2, 3]
print(sequence[2:])                        # [2, 3, 4, 5, 6]
print(sequence[::2])                       # [0, 2, 4, 6]
print(sequence[::-1])                      # 倒序

exercise_text = "万过薪月，员序程马黑来，nohtyP学"
print(exercise_text[::-1][9:14])           # 黑马程序员


show_title("6. 第 73～74 集：集合")

# 空集合必须写 set()；{} 表示空字典。
my_set_demo = {"传智教育", "黑马程序员", "itheima", "黑马程序员"}
print("自动去重：", my_set_demo)

my_set_demo.add("Python")
my_set_demo.remove("itheima")
print("添加和删除后：", my_set_demo)

set1 = {1, 2, 3}
set2 = {2, 3, 4}
print("差集 set1 - set2：", set1.difference(set2))       # {1}
print("交集：", set1.intersection(set2))                 # {2, 3}
print("并集：", set1.union(set2))                        # {1, 2, 3, 4}

# difference_update 会直接修改原集合；difference 只返回新集合。
set_copy = set1.copy()
set_copy.difference_update(set2)
print("difference_update 后：", set_copy)

# 集合无序、不支持下标，但可以使用 for 遍历。
for item in sorted(my_set_demo):
    print("集合元素：", item)


show_title("7. 第 75～77 集：字典")

# 字典通过键读取值；键不能重复，重复赋值会覆盖旧值。
student_scores = {"小明": 88, "小红": 95, "小刚": 76}
print("小红成绩：", student_scores["小红"])
print("不存在时使用默认值：", student_scores.get("小李", 0))

student_scores["小王"] = 85               # 新增
student_scores["小明"] = 90               # 修改
removed_score = student_scores.pop("小刚") # 删除并返回值
print("删除的小刚成绩：", removed_score)
print("所有键：", list(student_scores.keys()))
print("所有值：", list(student_scores.values()))
print("所有键值对：", list(student_scores.items()))

for student_name, score in student_scores.items():
    print(f"{student_name}：{score}")

# 嵌套字典适合保存有结构的数据。
employees = {
    "王力宏": {"department": "科技部", "salary": 3000, "level": 1},
    "周杰伦": {"department": "市场部", "salary": 5000, "level": 2},
    "林俊杰": {"department": "市场部", "salary": 7000, "level": 3},
}

# 课程练习：所有级别为 1 的员工升一级，并加薪 1000 元。
for employee_info in employees.values():
    if employee_info["level"] == 1:
        employee_info["level"] += 1
        employee_info["salary"] += 1000

print("加薪后的员工信息：", employees)


show_title("8. 第 78 集：五类数据容器概览")

# 列表：有序、可修改、允许重复。
my_list = [3, 1, 2, 2]

# 元组：有序、不可修改、允许重复。
my_tuple = (3, 1, 2, 2)

# 字符串：有序、不可修改，本质上是字符序列。
my_string = "python"

# 集合：无序、可修改、不允许重复，因此两个 2 最终只保留一个。
my_set = {3, 1, 2, 2}

# 字典：使用“键: 值”保存数据；键不能重复。
my_dict = {"name": "小明", "age": 18}

print("列表：", my_list)
print("元组：", my_tuple)
print("字符串：", my_string)
print("集合（显示顺序不保证固定）：", my_set)
print("字典：", my_dict)


show_title("9. 第 79 集：通用操作 len、max、min")

numbers = [10, 30, 20, 5]
print("元素数量：", len(numbers))       # 4
print("最大值：", max(numbers))         # 30
print("最小值：", min(numbers))         # 5

# 字典参与 len 时统计键值对数量；参与 max/min 时比较的是“键”。
scores = {"A": 90, "C": 80, "B": 95}
print("字典长度：", len(scores))         # 3
print("最大的键：", max(scores))         # C
print("最小的键：", min(scores))         # A


show_title("10. list()：转换成列表")

print(list((10, 20, 30)))                # [10, 20, 30]
print(list("abc"))                       # ['a', 'b', 'c']
print(list({10, 20, 30}))                # 顺序不保证固定
print(list({"name": "小明", "age": 18}))  # 字典转列表，只得到键


show_title("11. tuple()：转换成元组")

print(tuple([10, 20, 30]))               # (10, 20, 30)
print(tuple("abc"))                      # ('a', 'b', 'c')


show_title("12. set()：转换成集合并去重")

repeated_numbers = [3, 1, 3, 2, 1]
unique_numbers = set(repeated_numbers)
print("去重后的集合：", unique_numbers)

# 如果最终还需要列表，可以再转换一次。注意：集合不保证原顺序。
unique_list = list(unique_numbers)
print("集合再转列表：", unique_list)

# 如果既要去重又要保持原顺序，可以使用下面的常见写法。
ordered_unique = list(dict.fromkeys(repeated_numbers))
print("保持原顺序去重：", ordered_unique)  # [3, 1, 2]


show_title("13. str()：转换成字符串")

number_text = str(123)
list_text = str([1, 2, 3])
print(number_text, type(number_text))     # 123 <class 'str'>
print(list_text, type(list_text))         # [1, 2, 3] <class 'str'>

# str(列表) 得到的是列表的“文字表示”，不是把元素无缝连接。
# 连接多个字符串应该使用 join()。
words = ["Python", "很", "有趣"]
print("-".join(words))                   # Python-很-有趣


show_title("14. sorted()：通用排序")

data = [3, 1, 4, 2]
ascending = sorted(data)
descending = sorted(data, reverse=True)

print("原列表：", data)                  # 原列表不会被 sorted 修改
print("升序结果：", ascending)            # [1, 2, 3, 4]
print("降序结果：", descending)           # [4, 3, 2, 1]

# sorted() 不管接收哪种可迭代容器，返回值都是列表。
print(sorted((3, 1, 2)))                  # [1, 2, 3]
print(sorted("python"))                   # ['h', 'n', 'o', 'p', 't', 'y']
print(sorted({3, 1, 2}))                  # [1, 2, 3]
print(sorted({"c": 3, "a": 1, "b": 2}))  # 对字典的键排序


show_title("15. sorted() 与 list.sort() 横向比较")

source = [3, 1, 2]
new_list = sorted(source)
print("sorted 后的原列表：", source)       # [3, 1, 2]
print("sorted 返回的新列表：", new_list)   # [1, 2, 3]

source.sort()
print("sort 修改原列表：", source)         # [1, 2, 3]

# 核心区别：
# sorted(容器)  -> 不修改原数据，返回一个新列表，可用于多种容器。
# 列表.sort()   -> 直接修改原列表，返回值是 None，只能由列表调用。


show_title("16. 第 80 集：字符串大小比较")

# Python 按字符的 Unicode 编码逐个比较，遇到第一组不同字符就能决定大小。
print("a" > "A")                         # True
print("abc" < "abd")                     # True，前两位相同，比较 c 和 d
print("ab" < "abc")                      # True，公共部分相同，较短者更小

# ord() 查看字符对应的编码；chr() 根据编码得到字符。
print("A 的编码：", ord("A"))             # 65
print("a 的编码：", ord("a"))             # 97
print("编码 65 对应：", chr(65))           # A


show_title("17. 五类容器横向比较")

comparison_rows = [
    ("list",  "有序", "可修改",   "允许重复",   "下标取值"),
    ("tuple", "有序", "不可修改", "允许重复",   "下标取值"),
    ("str",   "有序", "不可修改", "字符可重复", "下标取字符"),
    ("set",   "无序", "可修改",   "自动去重",   "不支持下标"),
    ("dict",  "插入有序", "可修改", "键不重复", "按键取值"),
]

print(f"{'类型':<10}{'顺序':<10}{'可变性':<10}{'重复性':<12}{'取值方式'}")
for row in comparison_rows:
    print(f"{row[0]:<10}{row[1]:<10}{row[2]:<10}{row[3]:<12}{row[4]}")

print("\n选择建议：经常增删改用 list；固定数据用 tuple；去重用 set；有名称的数据用 dict。")
