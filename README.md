# Python 入门课程笔记

这是一套按知识点整理的 Python 学习示例。代码以课程章节为主线，每个主题单独存放，既可以配合视频学习，也可以在需要时当作基础知识速查。

示例尽量保持短小，重要语法配有中文注释；列表、元组、字符串、集合、字典等相近概念还放在一起做了对比，方便理解它们各自适合的场景。

## 内容概览

目前收录黑马程序员 Python 入门课程 `BV1qW4y1a7fU` 的第 **18～110 集**和第 **127～164 集**，主要包括：

- Python 基础语法、条件判断、循环和函数
- 列表、元组、字符串、集合、字典
- 文件操作、异常、模块和包
- JSON 与 pyecharts 数据可视化
- SQL、MySQL 和 PySpark
- 闭包、装饰器、常用设计模式
- 多线程、Socket、正则表达式和递归

详细的章节索引见 [python_course/README.md](python_course/README.md)。

仓库还收录了莫烦 Python《Numpy & Pandas 数据处理教程》`BV1Ex411L7oT` 的完整 18 集笔记，详见 [numpy和pandas学习/README.md](numpy和pandas学习/README.md)。

## 目录结构

```text
python_study/
├── python_class.ipynb     # 补充练习与 Notebook 记录
├── python_course/         # 按知识点分类的课程代码
│   ├── 01_基础语法_类型转换与字符串/
│   ├── 02_布尔值与条件判断/
│   ├── 03_循环语句/
│   ├── 04_函数基础/
│   ├── 05_列表元组字符串集合字典/
│   ├── 06_函数进阶/
│   ├── 07_文件操作/
│   ├── 08_异常模块与包/
│   ├── 09_JSON与折线图/
│   ├── 10_地图可视化/
│   ├── 11_柱状图与时间线/
│   ├── 12_SQL与MySQL/
│   ├── 13_PySpark大数据处理/
│   ├── 14_闭包装饰器与设计模式/
│   ├── 15_多线程编程/
│   ├── 16_Socket网络编程/
│   ├── 17_正则表达式/
│   └── 18_递归/
├── numpy和pandas学习/      # NumPy 与 Pandas 18 集交互式 Notebook
├── .gitignore
└── README.md
```

## 快速开始

准备 Python 3.9 或更高版本，然后克隆仓库：

```bash
git clone https://github.com/lzynb0206/python-course-notes.git
cd python-course-notes
```

大部分章节只使用 Python 标准库，可以直接运行：

```bash
python3 "python_course/01_基础语法_类型转换与字符串/第18-28集_基础语法.py"
python3 "python_course/05_列表元组字符串集合字典/第62-80集_数据容器.py"
python3 "python_course/14_闭包装饰器与设计模式/第154-157集_高级语法与设计模式.py"
```

运行 NumPy 和 Pandas 专题前，先安装对应依赖：

```bash
python3 -m pip install -r "numpy和pandas学习/requirements.txt"
python3 -m jupyter lab
```

运行数据可视化示例前，需要安装 pyecharts：

```bash
python3 -m pip install -r python_course/requirements.txt
```

MySQL 和 PySpark 属于可选内容，需要时再安装对应依赖：

```bash
python3 -m pip install -r python_course/requirements-advanced.txt
```

## 章节索引

| 集数 | 内容 |
|---:|---|
| 18～28 | 类型转换、运算符、字符串格式化与输入 |
| 29～37 | 布尔值与条件判断 |
| 38～50 | `while`、`for`、`range` 与循环控制 |
| 51～61 | 函数、参数、返回值与作用域 |
| 62～80 | 列表、元组、字符串、集合与字典 |
| 81～84 | 多返回值、`*args`、`**kwargs` 与 Lambda |
| 85～90 | 文件读取、写入、追加与综合练习 |
| 91～98 | 异常、模块、自定义包与第三方包 |
| 99～104 | JSON、数据清洗与折线图 |
| 105～107 | 地图可视化 |
| 108～110 | 柱状图、时间线与动态 GDP 图 |
| 127～138 | SQL、MySQL 与 Python 数据库操作 |
| 139～153 | PySpark RDD、常用算子与综合练习 |
| 154～157 | 闭包、装饰器、单例模式与工厂模式 |
| 158～159 | 多线程与线程同步 |
| 160～161 | Socket 服务端与客户端 |
| 162～163 | 正则表达式基础与元字符 |
| 164 | 递归 |

## 运行说明

- SQL 示例默认只展示语句，不会连接或修改数据库。要连接本机 MySQL，可在对应文件中填写自己的连接信息并打开运行开关。
- PySpark 章节提供了可直接运行的 Python 对照示例；真实 Spark 示例需要额外准备 Java 和 PySpark 环境。
- 文件操作和递归示例产生的练习文件会保存在各章节的 `runtime_data/` 中。
- 可视化示例生成的 HTML 会保存在相应章节的 `outputs/` 中。
- `runtime_data/`、生成的 HTML、虚拟环境和 IDE 配置均已加入 `.gitignore`。

第 111～126 集目前尚未整理。仓库中的疫情和 GDP 数据是为了演示处理流程而准备的小型样例，不应作为现实统计数据使用。

## 课程来源

- [黑马程序员 Python 教程](https://www.bilibili.com/video/BV1qW4y1a7fU)
- [莫烦 Python：Numpy & Pandas 数据处理教程](https://www.bilibili.com/video/BV1Ex411L7oT)

本仓库仅用于学习与交流，课程内容版权归原作者所有。
