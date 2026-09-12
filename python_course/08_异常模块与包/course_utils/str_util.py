"""字符串工具模块：对应第 98 集综合案例。"""

# 使用 from course_utils.str_util import * 时，只导入这两个函数。
__all__ = ["str_reverse", "substr"]


def str_reverse(text):
    """使用切片 [::-1] 反转字符串。"""
    return text[::-1]


def substr(text, start, end):
    """取得 text 从 start 开始、到 end 之前结束的子串。"""
    return text[start:end]


if __name__ == "__main__":
    # 直接运行本模块时执行测试；被其他文件导入时不执行。
    print(str_reverse("黑马程序员"))
    print(substr("itheima", 0, 2))

