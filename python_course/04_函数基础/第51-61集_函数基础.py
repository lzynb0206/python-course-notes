"""
第 51～61 集：函数定义、参数、返回值、None、说明文档、嵌套调用、作用域和 ATM 案例。
"""


def show_title(title):
    print(f"\n{'=' * 12} {title} {'=' * 12}")


show_title("1. 第 51～52 集：函数初体验与基础定义")


def say_hello():
    """无参数、无显式返回值的函数。"""
    print("欢迎学习 Python")


# 定义函数时不会执行函数体，调用函数时才执行。
say_hello()
say_hello()


show_title("2. 第 53 集：自动查核酸练习")


def check_temperature_message():
    print("欢迎来到黑马程序员！")
    print("请出示您的健康码以及 72 小时核酸证明！")


check_temperature_message()


show_title("3. 第 54～55 集：函数参数")


def add(x, y):
    # x、y 是形式参数；调用时传入的 10、20 是实际参数。
    result = x + y
    print(f"{x} + {y} = {result}")


add(10, 20)


def check_temperature(temperature):
    print(f"体温测量中，您的体温是：{temperature}℃")
    if temperature <= 37.5:
        print("体温正常，请进！")
    else:
        print("体温异常，需要隔离！")


check_temperature(36.8)
check_temperature(38.2)


show_title("4. 第 56 集：返回值")


def calculate_sum(x, y):
    """return 把结果交回调用处，同时立即结束函数。"""
    return x + y
    print("return 后的代码不会执行")


answer = calculate_sum(5, 8)
print("返回值：", answer)                  # 13

# print 是“展示结果”；return 是“把结果交给调用者继续使用”。


show_title("5. 第 57 集：None 类型")


def no_return_value():
    print("函数没有写 return")


result = no_return_value()
print("返回内容：", result)                # None
print("返回类型：", type(result))          # <class 'NoneType'>


def find_name(names, target):
    if target in names:
        return target
    return None                             # 表示没有找到、没有结果


print(find_name(["小明", "小红"], "小刚"))


show_title("6. 第 58 集：函数说明文档")


def subtract(x, y):
    """
    计算两个数字的差。

    :param x: 被减数
    :param y: 减数
    :return: x - y 的结果
    """
    return x - y


print(subtract(10, 3))
print("函数说明：", subtract.__doc__.strip().splitlines()[0])


show_title("7. 第 59 集：函数嵌套调用")


def function_b():
    print("2. 进入 function_b")
    print("3. 离开 function_b")


def function_a():
    print("1. 进入 function_a")
    function_b()
    print("4. 离开 function_a")


function_a()

# function_a 会暂停在调用 function_b 的位置；function_b 完成后，再回到 function_a。


show_title("8. 第 60 集：局部变量与全局变量")

global_number = 100


def read_global():
    local_number = 20                       # 局部变量，只在当前函数内部使用
    print("函数内读取全局变量：", global_number)
    print("函数内局部变量：", local_number)


def change_global():
    global global_number                    # 声明要修改函数外的同名变量
    global_number = 200


read_global()
change_global()
print("修改后的全局变量：", global_number)

# 实际开发应减少直接修改全局变量，但课程 ATM 案例会用它练习作用域。


show_title("9. 第 61 集：ATM 综合案例")

account_balance = 5000000
account_name = "小明"


def show_account_header():
    print(f"欢迎您，{account_name}")


def query_balance(show_header=True):
    if show_header:
        show_account_header()
    print(f"您的余额是：{account_balance} 元")


def deposit(amount):
    global account_balance
    show_account_header()
    account_balance += amount
    print(f"存款 {amount} 元成功")
    query_balance(show_header=False)


def withdraw(amount):
    global account_balance
    show_account_header()

    if amount > account_balance:
        print("余额不足，取款失败")
        return False

    account_balance -= amount
    print(f"取款 {amount} 元成功")
    query_balance(show_header=False)
    return True


# 用固定调用模拟菜单操作：查询 -> 存款 -> 取款。
query_balance()
deposit(1000)
withdraw(2000)


show_title("10. 函数知识横向总结")

print("参数：外部交给函数的数据")
print("返回值：函数处理后交回外部的数据")
print("None：没有具体返回结果")
print("局部变量：只在函数内部生效")
print("全局变量：整个模块可见，修改时需要 global")
print("说明文档：用三引号解释函数用途、参数和返回值")

