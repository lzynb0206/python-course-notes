"""
第 29～37 集：布尔类型、比较运算符、if/else/elif、嵌套判断和综合案例。

示例使用固定数据，运行时不会要求输入；可以修改变量观察分支变化。
"""


def show_title(title):
    print(f"\n{'=' * 12} {title} {'=' * 12}")


show_title("1. 第 29 集：布尔类型和比较运算符")

# 布尔值只有 True 和 False，首字母必须大写。
print(True, type(True))
print(False, type(False))

a = 10
b = 5
print("等于：", a == b)                   # False
print("不等于：", a != b)                 # True
print("大于：", a > b)                    # True
print("小于：", a < b)                    # False
print("大于等于：", a >= b)               # True
print("小于等于：", a <= b)               # False


show_title("2. 第 30～31 集：if 与成年人判断")

age = 20

# if 条件后面必须有冒号；属于 if 的代码必须缩进。
if age >= 18:
    print("已经成年，需要对自己的行为负责")

print("这行没有缩进，所以无论条件真假都会执行")


show_title("3. 第 32～33 集：if else 与买票案例")

height = 125

if height > 120:
    print("身高超过 120cm，需要买票")
else:
    print("身高不超过 120cm，可以免费")

# if 和 else 只会执行其中一个分支。


show_title("4. 第 34 集：if elif else 多条件判断")

score = 87

if score >= 90:
    level = "优秀"
elif score >= 80:
    level = "良好"
elif score >= 60:
    level = "及格"
else:
    level = "不及格"

print(f"成绩 {score}，等级：{level}")

# 判断从上到下进行，一旦某个条件为 True，后面的 elif/else 就不会执行。
# 所以范围通常从要求最高的条件开始写。


show_title("5. 第 35 集：猜数字案例")

target_number = 10
guess = 8

if guess == target_number:
    print("一次猜对")
elif guess > target_number:
    print("猜大了")
else:
    print("猜小了")


show_title("6. 第 36 集：嵌套判断")

age = 19
height = 175

if age >= 18:
    print("年龄条件满足")
    if height >= 170:
        print("并且身高达到 170cm")
    else:
        print("但身高没有达到 170cm")
else:
    print("年龄未满 18 岁")

# 内层 if 只有在外层条件满足时才有机会运行。
# 每增加一层嵌套，就多缩进 4 个空格。


show_title("7. 逻辑运算符：and、or、not")

temperature = 36.5
has_ticket = True

print(temperature < 37.3 and has_ticket)   # 两边都为 True 才是 True
print(temperature >= 37.3 or not has_ticket)  # 任意一边为 True 就是 True
print(not has_ticket)                      # 对布尔值取反


show_title("8. 第 37 集：三次猜数字综合案例")


def check_three_guesses(target, guesses):
    """使用三层判断模拟课程的三次猜数字流程。"""
    if guesses[0] == target:
        return "第一次猜对了"

    print("第一次猜错")
    if guesses[1] == target:
        return "第二次猜对了"

    print("第二次猜错")
    if guesses[2] == target:
        return "第三次猜对了"

    return f"三次都没猜对，正确数字是 {target}"


print(check_three_guesses(10, [5, 12, 10]))


show_title("9. 条件结构横向比较")

print("if：条件成立时执行，可以单独存在")
print("if/else：两个互斥分支，必定执行一个")
print("if/elif/else：多个互斥分支，从上到下匹配")
print("嵌套 if：先满足外层条件，再判断更细的内层条件")

