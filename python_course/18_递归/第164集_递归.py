"""
第 164 集：递归。

递归是函数直接或间接调用自身。正确的递归必须包含：
1. 终止条件（最小问题，不再继续调用）；2. 递归步骤（问题规模不断缩小）。
"""

from pathlib import Path


def show_title(title):
    print(f"\n{'=' * 12} {title} {'=' * 12}")


show_title("1. 阶乘：最小递归示例")


def factorial(number):
    """计算 number!，例如 5! = 5 × 4 × 3 × 2 × 1。"""
    if number < 0:
        raise ValueError("阶乘只接受非负整数")
    if number in (0, 1):
        return 1                         # 终止条件
    return number * factorial(number - 1)  # 递归步骤：问题从 n 缩小为 n-1


print("5! =", factorial(5))             # 120


show_title("2. 递归查找目录中的文件")


def find_files(directory, suffix=".txt"):
    """递归找到 directory 及其子目录里指定后缀的所有文件。"""
    directory = Path(directory)
    if not directory.exists():
        return []

    matched_files = []
    for item in directory.iterdir():
        if item.is_file() and item.suffix == suffix:
            matched_files.append(item)              # 当前层直接解决
        elif item.is_dir():
            matched_files.extend(find_files(item, suffix))  # 子目录交给递归
    return matched_files


# 创建一个只用于演示的小目录；runtime_data 已被 .gitignore 忽略。
base_dir = Path(__file__).resolve().parent
demo_dir = base_dir / "runtime_data" / "递归示例"
(demo_dir / "第一层" / "第二层").mkdir(parents=True, exist_ok=True)
(demo_dir / "根目录.txt").write_text("root", encoding="utf-8")
(demo_dir / "第一层" / "笔记.txt").write_text("note", encoding="utf-8")
(demo_dir / "第一层" / "图片.png").write_text("demo", encoding="utf-8")
(demo_dir / "第一层" / "第二层" / "练习.txt").write_text("practice", encoding="utf-8")

for file_path in sorted(find_files(demo_dir)):
    print(file_path.relative_to(demo_dir))


show_title("3. 递归与循环横向比较")

comparison = [
    ("递归", "树、目录、嵌套结构", "表达自然，但调用层数过深会报错"),
    ("循环", "线性重复、计数", "通常更省内存，也没有递归深度问题"),
]
for method, suitable_for, feature in comparison:
    print(f"{method:<4} | {suitable_for:<12} | {feature}")

# Python 默认会限制递归深度，因此不要用递归处理无限或极深的数据。
# 调试递归时可以检查：参数是否越来越接近终止条件？每一层是否正确返回结果？
