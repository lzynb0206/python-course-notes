"""
第 91～98 集：异常、模块、包和综合案例。

本文件会调用同目录中的 course_utils 自定义包。
"""

import math
from pathlib import Path

from course_utils import file_util
from course_utils.str_util import str_reverse, substr


BASE_DIR = Path(__file__).resolve().parent
RUNTIME_DIR = BASE_DIR / "runtime_data"
RUNTIME_DIR.mkdir(exist_ok=True)


def show_title(title):
    print(f"\n{'=' * 12} {title} {'=' * 12}")


show_title("1. 第 91 集：认识异常")

# 异常是程序运行期间出现的问题。下面故意产生异常，但会立即捕获，所以程序不会中断。
try:
    number = int("不是数字")
except ValueError as error:
    print("捕获到 ValueError：", error)

# 常见异常：
# NameError          使用了未定义变量
# ZeroDivisionError  除数为 0
# ValueError         值不符合转换要求
# TypeError          数据类型不支持某种操作
# IndexError         列表/元组下标越界
# KeyError           字典中没有指定键
# FileNotFoundError  文件不存在


show_title("2. 第 92 集：异常捕获的完整结构")


def divide_from_text(text, divisor):
    try:
        number = int(text)
        result = number / divisor
    except ValueError as error:
        print("无法把文字转换成整数：", error)
    except ZeroDivisionError as error:
        print("除数不能是 0：", error)
    except Exception as error:
        # Exception 能捕获绝大多数常规异常，应当放在更具体的 except 后面。
        print("发生其他异常：", error)
    else:
        # try 中没有异常才执行 else。
        print("计算成功：", result)
    finally:
        # 无论是否发生异常都会执行，常用于关闭文件等清理工作。
        print("本次计算结束")


divide_from_text("20", 4)
divide_from_text("abc", 4)
divide_from_text("20", 0)


show_title("3. 第 93 集：异常的传递性")


def level_3():
    return 10 / 0


def level_2():
    return level_3()


def level_1():
    return level_2()


try:
    level_1()
except ZeroDivisionError:
    print("异常从 level_3 逐层传递，最终在最外层被捕获")

# 异常可以在发生处捕获，也可以交给调用者处理。
# 实际项目常在能够“合理处理问题”的那一层捕获。


show_title("4. 第 94 集：模块的概念和导入")

# 一个 .py 文件就是一个模块。Python 标准库已经提供了许多模块。
print("math.sqrt(16) =", math.sqrt(16))

# 常见导入形式：
# import 模块名
# import 模块名 as 别名
# from 模块名 import 功能名
# from 模块名 import 功能名 as 别名
# 不建议随意使用 from 模块名 import *，因为容易产生命名冲突。


show_title("5. 第 95～96 集：自定义模块和包")

print(str_reverse("黑马程序员"))           # 员序程马黑
print(substr("itheima", 0, 2))            # it，切片左闭右开

# course_utils/ 是一个包，里面的 str_util.py、file_util.py 是模块。
# __init__.py 用于标识和初始化包；__all__ 可以控制 import * 公开的名称。
# 模块里的 if __name__ == "__main__" 测试代码在导入时不会运行。


show_title("6. 第 97 集：第三方包")

print("第三方包不是 Python 自带的，通常使用下面的命令安装：")
print("python3 -m pip install pyecharts")
print("如果 PyCharm 仍提示找不到包，要检查 pip 和项目是否使用同一个解释器。")


show_title("7. 第 98 集：异常、模块、包综合案例")

demo_file = RUNTIME_DIR / "module_demo.txt"
demo_file.write_text("第一行\n", encoding="utf-8")

file_util.append_to_file(demo_file, "第二行：由 append_to_file 追加\n")
file_util.print_file_info(demo_file)

# 再演示不存在的文件。工具函数会自行捕获异常，不会让主程序崩溃。
file_util.print_file_info(RUNTIME_DIR / "not_found.txt")

print("\n模块、包层级：主程序 -> course_utils 包 -> str_util/file_util 模块 -> 函数")

