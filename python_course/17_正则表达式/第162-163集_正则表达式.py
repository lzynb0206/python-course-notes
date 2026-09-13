"""
第 162～163 集：正则表达式基础与元字符。

正则表达式用于按“规则”匹配文本。规则字符串通常使用 r"..." 原始字符串，
避免反斜杠同时被 Python 字符串和正则表达式解释。
"""

import re


def show_title(title):
    print(f"\n{'=' * 12} {title} {'=' * 12}")


show_title("1. 第 162 集：match、search、findall")

text = "Python 3.10，联系电话 13812345678，备用电话 13987654321"

# match 只从字符串开头匹配。
match_result = re.match(r"Python", text)
print("match：", match_result.group() if match_result else "未匹配")

# search 在整个字符串中寻找第一个匹配。
search_result = re.search(r"\d+\.\d+", text)
print("search：", search_result.group() if search_result else "未匹配")

# findall 返回所有匹配到的字符串。
phone_numbers = re.findall(r"1[3-9]\d{9}", text)
print("findall：", phone_numbers)


show_title("2. 第 163 集：字符类与数量限定")

examples = [
    (r"\d", "一个数字，等价于 [0-9]"),
    (r"\D", "一个非数字"),
    (r"\w", "一个字母、数字或下划线等单词字符"),
    (r"\s", "一个空白字符"),
    (r".", "除换行外的任意字符"),
    (r"[abc]", "a、b、c 中任意一个"),
    (r"[^abc]", "除 a、b、c 以外的任意字符"),
    (r"a*", "a 出现 0 次或多次"),
    (r"a+", "a 出现 1 次或多次"),
    (r"a?", "a 出现 0 次或 1 次"),
    (r"a{3}", "a 恰好出现 3 次"),
    (r"a{2,4}", "a 出现 2～4 次"),
]
for pattern, meaning in examples:
    print(f"{pattern:<10} | {meaning}")


show_title("3. 边界、分组与或")

# ^ 匹配开头，$ 匹配结尾；二者结合适合验证“整个字符串”。
username_pattern = re.compile(r"^[A-Za-z][A-Za-z0-9_]{5,11}$")
for username in ("python_01", "1python", "py"):
    print(username, "->", bool(username_pattern.fullmatch(username)))

# () 用于分组和捕获，| 表示“或者”。
date_text = "今天是 2026-09-13"
date_result = re.search(r"(\d{4})-(\d{2})-(\d{2})", date_text)
if date_result:
    print("完整日期：", date_result.group(0))
    print("年/月/日：", date_result.groups())

language_result = re.search(r"Python|Java", "我正在学习 Python")
print("或规则：", language_result.group() if language_result else "未匹配")


show_title("4. 综合练习：邮箱验证和信息提取")

# 这是适合教学的简化邮箱规则，不代表互联网所有合法邮箱格式。
email_pattern = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")
emails = ["student@example.com", "wrong@email", "python.course@school.cn"]
for email in emails:
    print(email, "->", "格式正确" if email_pattern.fullmatch(email) else "格式错误")

log = "name=小明 age=18 score=92"
fields = dict(re.findall(r"(\w+)=([^\s]+)", log))
print("提取字段：", fields)


show_title("5. 三个查找函数横向比较")

comparison = [
    ("re.match", "只从开头找", "Match 或 None"),
    ("re.search", "全文找第一个", "Match 或 None"),
    ("re.findall", "全文找全部", "列表"),
    ("re.fullmatch", "整个字符串必须符合", "Match 或 None"),
]
for function_name, range_description, result_type in comparison:
    print(f"{function_name:<13} | {range_description:<10} | {result_type}")
