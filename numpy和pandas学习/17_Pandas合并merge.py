"""第 17 集：使用 merge 按键关联两张表。"""

import pandas as pd


students = pd.DataFrame(
    {
        "student_id": [1, 2, 3, 4],
        "name": ["小明", "小红", "小刚", "小兰"],
        "class_id": ["A", "A", "B", "C"],
    }
)
scores = pd.DataFrame(
    {
        "student_id": [1, 2, 2, 5],
        "subject": ["Python", "Python", "SQL", "Python"],
        "score": [88, 95, 90, 77],
    }
)
print("学生表：\n", students)
print("\n成绩表：\n", scores)


print("\n1. inner：只保留两边都能匹配的键")
inner = pd.merge(students, scores, on="student_id", how="inner")
print(inner)


print("\n2. left：完整保留左表")
left = pd.merge(students, scores, on="student_id", how="left")
print(left)


print("\n3. outer：保留两边所有键，并标记来源")
outer = pd.merge(
    students,
    scores,
    on="student_id",
    how="outer",
    indicator=True,
)
print(outer)
print("来源统计：\n", outer["_merge"].value_counts())


print("\n4. 多个键共同匹配")
planned = pd.DataFrame(
    {
        "student_id": [1, 1, 2],
        "subject": ["Python", "SQL", "Python"],
        "hours": [20, 15, 25],
    }
)
actual = pd.DataFrame(
    {
        "student_id": [1, 2, 2],
        "subject": ["Python", "Python", "SQL"],
        "finished": [True, True, False],
    }
)
print(pd.merge(planned, actual, on=["student_id", "subject"], how="outer"))


print("\n5. 按索引合并")
class_names = pd.DataFrame(
    {"class_name": ["基础班", "进阶班", "项目班"]},
    index=pd.Index(["A", "B", "C"], name="class_id"),
)
students_by_class = students.set_index("class_id")
print(pd.merge(students_by_class, class_names, left_index=True, right_index=True))


print("\n6. 重名列使用 suffixes")
boys = pd.DataFrame({"key": ["K0", "K1"], "age": [18, 20]})
girls = pd.DataFrame({"key": ["K0", "K0"], "age": [19, 21]})
print(pd.merge(boys, girls, on="key", suffixes=("_boy", "_girl")))


print("\n7. validate 检查键关系")
unique_profiles = pd.DataFrame({"student_id": [1, 2, 3], "city": ["北京", "上海", "广州"]})
checked = pd.merge(
    scores,
    unique_profiles,
    on="student_id",
    how="left",
    validate="many_to_one",  # 成绩表可重复，档案表的键必须唯一
)
print(checked)

print("\n关联类型速记：inner=交集，left=保留左表，right=保留右表，outer=并集")
