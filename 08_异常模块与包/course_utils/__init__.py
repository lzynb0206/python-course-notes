"""第 96～98 集示例包。存在 __init__.py 的目录可以作为普通 Python 包导入。"""

# 使用 from course_utils import * 时，只公开下面两个模块名。
__all__ = ["str_util", "file_util"]

