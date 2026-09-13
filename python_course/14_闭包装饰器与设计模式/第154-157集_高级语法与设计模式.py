"""
第 154～157 集：闭包、装饰器、单例模式和工厂模式。

这四个知识点都在回答同一个问题：怎样把代码组织得更灵活、更容易复用。
"""

from functools import wraps


def show_title(title):
    print(f"\n{'=' * 12} {title} {'=' * 12}")


show_title("1. 第 154 集：闭包")


def make_account(initial_balance):
    """外层函数结束后，内层函数仍能记住 balance，这就是闭包。"""
    balance = initial_balance

    def deposit(amount):
        nonlocal balance
        # nonlocal 表示要修改外层函数的变量，而不是创建新的局部变量。
        if amount <= 0:
            raise ValueError("存款金额必须大于 0")
        balance += amount
        return balance

    return deposit


account_a = make_account(100)
account_b = make_account(500)
print("账户 A 存入 50：", account_a(50))    # 150
print("账户 A 再存 20：", account_a(20))    # 170，记住上次的状态
print("账户 B 存入 10：", account_b(10))    # 510，两个闭包状态互不影响

# 闭包适合保存少量私有状态、生成配置好的函数。
# 如果状态很多、行为复杂，使用类通常更清晰。


show_title("2. 第 155 集：装饰器")


def log_call(func):
    """不修改原函数源码，为函数增加调用日志。"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"准备调用 {func.__name__}，参数={args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} 调用结束，返回值={result}")
        return result

    return wrapper


@log_call
def add(left, right):
    """返回两个数字的和。"""
    return left + right


print("计算结果：", add(10, 20))
print("保留的函数名：", add.__name__)       # wraps 让名称仍然是 add

# @log_call 等价于：add = log_call(add)
# wrapper 使用 *args 和 **kwargs，因此能接收不同形式的参数。


def repeat(times):
    """带参数的装饰器：外层先接收装饰器配置。"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(times):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator


@repeat(times=2)
def greet(name):
    print(f"你好，{name}")


greet("Python")


show_title("3. 第 156 集：单例模式")


class AppConfig:
    """无论实例化多少次，都返回同一个对象。"""
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.theme = "light"
        return cls._instance


config_a = AppConfig()
config_b = AppConfig()
config_a.theme = "dark"
print("是否同一对象：", config_a is config_b)  # True
print("共享配置：", config_b.theme)             # dark

# 单例适合“整个程序只需要一份”的对象，如配置中心。
# 不要把所有对象都做成单例，否则会产生隐式共享状态，测试也更困难。


show_title("4. 第 157 集：工厂模式")


class Animal:
    def speak(self):
        raise NotImplementedError


class Cat(Animal):
    def speak(self):
        return "喵"


class Dog(Animal):
    def speak(self):
        return "汪"


class AnimalFactory:
    """由工厂根据名称决定创建哪个具体类。"""
    @staticmethod
    def create(animal_type):
        classes = {"cat": Cat, "dog": Dog}
        try:
            animal_class = classes[animal_type.lower()]
        except KeyError as error:
            raise ValueError(f"不支持的动物类型：{animal_type}") from error
        return animal_class()


for kind in ("cat", "dog"):
    animal = AnimalFactory.create(kind)
    print(f"{kind} -> {type(animal).__name__} -> {animal.speak()}")


show_title("5. 横向比较")

comparison = [
    ("闭包", "函数记住外层状态", "计数器、配置好的函数"),
    ("装饰器", "给函数增加通用行为", "日志、权限、计时"),
    ("单例", "控制同一类只有一个实例", "全局配置"),
    ("工厂", "集中管理对象创建逻辑", "按类型创建不同对象"),
]
for name, idea, use_case in comparison:
    print(f"{name:<4} | {idea:<14} | {use_case}")
