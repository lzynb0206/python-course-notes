"""
第 18～28 集：数据类型转换、标识符、运算符、字符串格式化、input。

本文件不直接调用 input()，避免运行时等待输入；最后提供了可自行取消注释的输入练习。
"""


def show_title(title):
    print(f"\n{'=' * 12} {title} {'=' * 12}")


show_title("1. 第 18 集：数据类型转换")

# int()：转换成整数。浮点数转整数会直接去掉小数部分，不是四舍五入。
print(int("123"), type(int("123")))       # 123 <class 'int'>
print(int(3.99))                           # 3

# float()：转换成浮点数。
print(float("12.5"), type(float("12.5"))) # 12.5 <class 'float'>
print(float(10))                           # 10.0

# str()：把数据转换成字符串，常用于拼接和输出。
print(str(100), type(str(100)))            # 100 <class 'str'>

# 只有符合数字格式的字符串才能转成数字。
try:
    int("12.5")
except ValueError as error:
    print("'12.5' 不能直接转成 int：", error)


show_title("2. 第 19 集：标识符与命名规范")

# 标识符是变量、函数、类等内容的名字。
# 规则：只能使用中文、英文、数字、下划线；不能以数字开头；区分大小写；不能使用关键字。
student_name = "小明"                    # 推荐：小写字母 + 下划线
student_age = 18
StudentAge = 20                            # 与 student_age 是不同名字，但不推荐这样命名变量
print(student_name, student_age, StudentAge)

# 常见错误示意（不要取消注释）：
# 2name = "小明"       # 不能以数字开头
# class = "一班"       # class 是 Python 关键字
# student-name = "小明" # 减号会被当成运算符


show_title("3. 第 20 集：算术运算符")

a = 10
b = 3
print("加法：", a + b)                    # 13
print("减法：", a - b)                    # 7
print("乘法：", a * b)                    # 30
print("除法：", a / b)                    # 3.333...
print("整除：", a // b)                   # 3
print("取余：", a % b)                    # 1
print("幂：", a ** b)                     # 1000

# 复合赋值运算符：先计算，再把结果保存回原变量。
number = 10
number += 5                                # 等价于 number = number + 5
number *= 2                                # 等价于 number = number * 2
print("复合赋值结果：", number)            # 30

# 计算顺序：括号 -> 幂 -> 乘除整除取余 -> 加减。
print("优先级：", 2 + 3 * 4)               # 14
print("使用括号：", (2 + 3) * 4)           # 20


show_title("4. 第 21 集：字符串的三种定义方式")

text1 = '单引号字符串'
text2 = "双引号字符串"
text3 = """三引号可以保存
多行内容"""
print(text1)
print(text2)
print(text3)

# 字符串中需要出现同种引号时，可以使用转义符 \。
quote1 = '他说："Python 很有趣"'
quote2 = "I'm learning Python"
quote3 = "他说：\"你好\""
print(quote1)
print(quote2)
print(quote3)


show_title("5. 第 22 集：字符串拼接")

name = "小明"
message = "你好，" + name + "，欢迎学习 Python"
print(message)

# 字符串只能直接和字符串拼接；数字需要先用 str() 转换。
age = 18
print("年龄：" + str(age))


show_title("6. 第 23～24 集：百分号格式化与精度控制")

name = "黑马程序员"
year = 2022
price = 19.9876

print("名称：%s，年份：%d，价格：%f" % (name, year, price))

# 格式：%宽度.精度f
# %5d  表示整数宽度为 5，不足时左侧补空格。
# %.2f 表示小数保留 2 位，会四舍五入。
# %8.2f 表示总宽度为 8，小数保留 2 位。
print("年份：%5d" % year)
print("价格：%.2f" % price)                # 19.99
print("价格：%8.2f" % price)


show_title("7. 第 25～26 集：f-string 与表达式格式化")

name = "小红"
age = 20
height = 1.678
print(f"姓名：{name}，年龄：{age}，身高：{height:.2f}米")

# 花括号中可以直接编写表达式。
print(f"10 + 20 = {10 + 20}")
print(f"明年年龄：{age + 1}")
print(f"名字长度：{len(name)}")


show_title("8. 第 27 集：股票价格计算练习")

stock_name = "传智播客"
stock_price = 19.99
stock_code = "003032"
stock_price_daily_growth_factor = 1.2
growth_days = 7
final_price = stock_price * stock_price_daily_growth_factor ** growth_days

print(f"公司：{stock_name}，股票代码：{stock_code}")
print(f"当前股价：{stock_price:.2f} 元")
print(f"每日增长系数：{stock_price_daily_growth_factor}，增长天数：{growth_days}")
print(f"计算后的股价：{final_price:.2f} 元")


show_title("9. 第 28 集：input 输入")

# input("提示语") 会暂停程序，等待用户输入，并且返回值永远是字符串 str。
# 本文件为了能够自动运行，先用字符串模拟用户输入。
simulated_input = "18"
print("模拟输入内容：", simulated_input, type(simulated_input))
input_age = int(simulated_input)
print("转换后的年龄：", input_age, type(input_age))

# 自己练习时可以取消下面三行的注释：
# user_name = input("请输入姓名：")
# user_age = int(input("请输入年龄："))
# print(f"你好，{user_name}，你明年 {user_age + 1} 岁")


show_title("10. 格式化方式横向比较")

score = 95.678
print("百分号方式：%.2f" % score)
print("format 方式：{:.2f}".format(score))
print(f"f-string 方式：{score:.2f}")
print("推荐优先掌握 f-string：结构最直观，也可以直接放入表达式。")

