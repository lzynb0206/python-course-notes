"""
第 81～84 集：函数进阶。

内容：
81 多返回值
82 位置参数、关键字参数、默认参数、*args、**kwargs
83 函数作为参数传递
84 Lambda 匿名函数
"""


def show_title(title):
    print(f"\n{'=' * 12} {title} {'=' * 12}")


show_title("1. 第 81 集：函数的多返回值")


def calculate(a, b):
    """用逗号返回多个值；本质上返回的是一个元组。"""
    return a + b, a - b, a * b


result = calculate(10, 3)
print(result, type(result))               # (13, 7, 30) <class 'tuple'>

# 元组拆包：变量数量要和返回值数量一致。
sum_result, difference, product = calculate(10, 3)
print(sum_result, difference, product)    # 13 7 30

# 下划线常用来接收“不打算使用”的返回值。
sum_result, _, product = calculate(8, 2)
print(sum_result, product)                # 10 16


show_title("2. 第 82 集：位置、关键字和默认参数")


def user_info(name, age, gender="男"):
    print(f"姓名={name}，年龄={age}，性别={gender}")


# 位置参数：按照参数出现的位置一一对应。
user_info("小明", 18)

# 关键字参数：根据名称对应，顺序可以改变。
user_info(age=20, name="小红", gender="女")

# 混合使用时，位置参数必须写在关键字参数前面。
user_info("小刚", age=19)


show_title("3. *args：不定长位置参数")


def add_all(*args):
    """定义时的 *args 会把所有额外位置参数收集成元组。"""
    print("args =", args, type(args))
    return sum(args)


print("求和：", add_all(10, 20, 30))      # 60

# 调用时的 * 是“拆包”：把列表/元组拆成多个位置参数。
numbers = [1, 2, 3, 4]
print("列表拆包后求和：", add_all(*numbers))  # 等价于 add_all(1, 2, 3, 4)


show_title("4. **kwargs：不定长关键字参数")


def show_profile(**kwargs):
    """定义时的 **kwargs 会把关键字参数收集成字典。"""
    print("kwargs =", kwargs, type(kwargs))
    print("姓名：", kwargs.get("name", "未填写"))
    print("城市：", kwargs.get("city", "未填写"))


show_profile(name="小明", age=18, city="郑州")

# 调用时的 ** 是“拆包”：把字典拆成关键字参数。
profile = {"name": "小红", "age": 20, "city": "洛阳"}
show_profile(**profile)

# 一定分清：
# def f(**kwargs) -> 收集，函数内部得到字典。
# f(**my_dict)    -> 拆开，字典键必须能作为参数名。


show_title("5. 各种参数横向比较")


def register(name, age=18, *hobbies, **other_info):
    print("name：", name)
    print("age：", age)
    print("hobbies：", hobbies)            # 元组
    print("other_info：", other_info)      # 字典


register("小明", 20, "编程", "篮球", city="北京", level="初级")


show_title("6. 第 83 集：函数作为参数传递")


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def compute(x, y, operation):
    """operation 接收一个函数；函数的处理逻辑可以由调用者决定。"""
    return operation(x, y)


# 注意传 add，不要写 add()。add 表示函数本身，add() 表示立即调用函数。
print(compute(10, 5, add))                # 15
print(compute(10, 5, subtract))           # 5


show_title("7. 第 84 集：Lambda 匿名函数")

# lambda 参数: 一行表达式
# Lambda 适合临时、简单、只写一行的函数。
print(compute(10, 5, lambda x, y: x * y))  # 50

students = [
    ["小明", 88],
    ["小红", 95],
    ["小刚", 76],
]

# key 函数告诉 sort：用每个小列表下标 1 的成绩作为排序依据。
students.sort(key=lambda student: student[1], reverse=True)
print("按成绩从高到低：", students)


show_title("8. Lambda 巩固：filter")

# 这一小节是对你之前问题的巩固：numbers 是完整列表，number 是每次取出的一个元素。
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda number: number % 2 == 0, numbers))
print(even_numbers)                       # [2, 4, 6]

# 普通函数更适合复杂逻辑；Lambda 更适合短小的一次性规则。

