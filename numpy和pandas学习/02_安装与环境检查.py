"""
第 2 集：安装 NumPy、Pandas，并检查当前环境。

学习目标：
1. 明白“Python 解释器”和“安装到该解释器的第三方包”是一套环境。
2. 学会使用 python -m pip，避免 pip 与 python 指向不同环境。
3. 能根据 ModuleNotFoundError 排查解释器配置。

虚拟环境的作用是把每个项目的依赖隔离开。仓库里的 .venv 只服务于本项目，
不会和系统 Python 或其他项目争用同一套包版本。
"""

import platform
import sys

import matplotlib
import numpy as np
import pandas as pd


print("Python：", sys.version.split()[0])
print("操作系统：", platform.platform())
print("NumPy：", np.__version__)
print("Pandas：", pd.__version__)
print("Matplotlib：", matplotlib.__version__)

# 推荐安装方式：
# python3 -m pip install -r "numpy和pandas学习/requirements.txt"
#
# 使用 python3 -m pip 而不是只写 pip，可以减少“包装到了另一个解释器”
# 这种常见问题。下面两个命令应指向同一个 Python 环境：
# python3 -c "import sys; print(sys.executable)"
# python3 -m pip --version


def environment_check():
    """执行最小计算，确认三个库不仅能导入，也能正常工作。"""
    array = np.array([1, 2, 3])
    frame = pd.DataFrame({"number": array})
    assert array.sum() == 6
    assert frame["number"].mean() == 2
    print("环境检查通过：", frame["number"].to_list())


environment_check()

# 遇到 ModuleNotFoundError 时，按下面的顺序排查：
# 1. 当前运行文件所使用的 Python 解释器路径。
# 2. 安装依赖时 python -m pip 所使用的解释器路径。
# 3. PyCharm 的项目解释器是否选择了仓库中的 .venv。
