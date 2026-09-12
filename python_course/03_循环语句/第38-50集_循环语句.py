"""
第 38～50 集：while、for、range、嵌套循环、continue、break 和综合案例。
"""

import random


def show_title(title):
    print(f"\n{'=' * 12} {title} {'=' * 12}")


show_title("1. 第 38 集：while 基础语法")

i = 1
while i <= 5:
    print(f"第 {i} 次学习 Python")
    i += 1                                 # 必须改变循环条件，避免死循环


show_title("2. 第 39 集：使用 while 求 1～100 的和")

number = 1
total = 0
while number <= 100:
    total += number
    number += 1

print("1～100 的和：", total)              # 5050


show_title("3. 第 40 集：while 猜数字")

target = 37
guesses = [20, 50, 37]                    # 用列表模拟三次输入
guess_count = 0
guessed = False

while not guessed and guess_count < len(guesses):
    guess = guesses[guess_count]
    guess_count += 1
    print(f"第 {guess_count} 次猜：{guess}")

    if guess == target:
        guessed = True
        print("猜对了")
    elif guess > target:
        print("猜大了")
    else:
        print("猜小了")

print("总共猜了：", guess_count, "次")


show_title("4. 第 41 集：while 嵌套")

day = 1
while day <= 3:
    lesson = 1
    while lesson <= 2:
        print(f"第 {day} 天，第 {lesson} 次练习")
        lesson += 1
    day += 1

# 外层循环每执行一次，内层循环会完整执行一遍。
# 每次进入新的外层循环时，内层计数器需要重新初始化。


show_title("5. 第 42 集：while 打印九九乘法表")

row = 1
while row <= 9:
    column = 1
    while column <= row:
        print(f"{column}×{row}={column * row}", end="\t")
        column += 1
    print()                                # 一行结束后换行
    row += 1


show_title("6. 第 43～44 集：for 循环与统计字母 a")

name = "itheima is a brand of itcast"
count = 0

for character in name:
    if character == "a":
        count += 1

print("字母 a 出现次数：", count)

# for 会依次取出字符串、列表等容器中的元素。
# 与 while 相比，for 更适合遍历已有容器或执行明确次数的任务。


show_title("7. 第 45 集：range")

print("range(5)：", list(range(5)))         # [0, 1, 2, 3, 4]
print("range(2, 6)：", list(range(2, 6)))   # [2, 3, 4, 5]
print("range(2, 10, 2)：", list(range(2, 10, 2)))  # [2, 4, 6, 8]

# range(start, stop, step) 左闭右开：包含 start，不包含 stop。


show_title("8. 第 46 集：for 临时变量作用域")

for temporary_number in range(3):
    print("循环内部：", temporary_number)

# Python 中循环变量在循环结束后仍然能访问，但不建议在外部依赖它。
print("循环结束后的临时变量：", temporary_number)


show_title("9. 第 47～48 集：for 嵌套与九九乘法表")

for row in range(1, 10):
    for column in range(1, row + 1):
        print(f"{column}×{row}={column * row}", end="\t")
    print()


show_title("10. 第 49 集：continue 与 break")

print("continue 跳过当前这一轮：")
for number in range(1, 6):
    if number == 3:
        continue
    print(number, end=" ")                  # 1 2 4 5
print()

print("break 直接结束当前循环：")
for number in range(1, 6):
    if number == 3:
        break
    print(number, end=" ")                  # 1 2
print()

# 在嵌套循环中，continue 和 break 默认只影响它们所在的最内层循环。


show_title("11. 第 50 集：发工资综合案例")

# 课程案例：公司有 20 名员工，总余额 10000 元；绩效不足 5 不发工资，余额不足则结束。
# 固定随机种子让每次运行结果相同，方便学习和检查。
random.seed(42)
company_balance = 10000
salary = 1000

for employee_id in range(1, 21):
    performance = random.randint(1, 10)

    if performance < 5:
        print(f"员工 {employee_id:02d}：绩效 {performance}，不发工资")
        continue

    if company_balance < salary:
        print("工资余额不足，停止发放")
        break

    company_balance -= salary
    print(
        f"员工 {employee_id:02d}：绩效 {performance}，"
        f"发放 {salary} 元，余额 {company_balance} 元"
    )

print("最终余额：", company_balance)


show_title("12. while 与 for 横向比较")

print("while：更适合循环次数不确定、由条件决定结束的任务")
print("for：更适合遍历容器，或配合 range 执行明确次数")
print("continue：跳过当前轮；break：结束当前循环")

