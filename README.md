# Python、NumPy 与 Pandas 学习笔记

这是我在学习 Python 和数据处理时整理的一套笔记，目前包含两门课程：Python 入门与进阶，以及 NumPy、Pandas 数据处理。

Python 部分以 `.py` 示例为主，适合跟着课程动手练习；NumPy 和 Pandas 部分使用 Jupyter Notebook，把知识点说明、代码、预期输出和容易混淆的地方放在一起。既可以按课程顺序学习，也可以在以后写代码时回来查阅。

## 学习内容

| 内容 | 课程范围 | 笔记形式 | 入口 |
|---|---|---|---|
| Python 基础与进阶 | 黑马程序员第 18～110、127～164 集 | 按知识点分类的 `.py` 文件 | [查看课程目录](python_course/README.md) |
| NumPy 与 Pandas | 莫烦 Python 完整 18 集 | 一集一本 `.ipynb` Notebook | [查看课程目录](numpy和pandas学习/README.md) |
| 补充练习 | 学习过程中随手记录 | Notebook | [打开补充笔记](python_class.ipynb) |

## 推荐学习顺序

如果是第一次系统学习，可以按下面的顺序进行：

1. 先学习 Python 基础语法、判断、循环和函数。
2. 掌握列表、元组、字符串、集合和字典，理解数据应该怎样保存和处理。
3. 学习文件、异常、模块和包，具备编写完整小程序的能力。
4. 进入 NumPy，学习数组、形状、批量运算、索引、合并、分割和复制。
5. 再学习 Pandas，处理表格选择、修改、缺失值、文件读写、表格合并和绘图。
6. 最后按需要学习数据库、PySpark、装饰器、多线程、网络编程和正则表达式。

这条路线中，Python 数据容器是 NumPy 和 Pandas 的基础；NumPy 的数组、索引和 `axis` 又是理解 Pandas 表格运算的基础。

## Python 课程索引

目前整理了 `BV1qW4y1a7fU` 的第 **18～110 集**和第 **127～164 集**。

| 集数 | 主要内容 |
|---:|---|
| 18～28 | 数据类型转换、运算符、字符串格式化与输入 |
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

列表、元组、字符串、集合和字典放在同一章节中横向比较，方便理解是否有序、能否修改、是否允许重复以及各自适合的使用场景。

## NumPy 与 Pandas 课程索引

`BV1Ex411L7oT` 的 18 集内容已经全部整理为 Notebook。笔记按照原学习记录展开，保留每个小知识点的解释、代码和预期结果。

| 集数 | 学习内容 | 笔记 |
|---:|---|---|
| 1～2 | NumPy、Pandas 的用途，安装与环境检查 | [从第 1 集开始](numpy和pandas学习/01_NumPy和Pandas有什么用.ipynb) |
| 3～4 | 数组的 `ndim`、`shape`、`size`、`dtype` 与数组创建 | [数组属性](numpy和pandas学习/03_NumPy数组属性.ipynb) · [创建数组](numpy和pandas学习/04_NumPy创建数组.ipynb) |
| 5～6 | 逐元素运算、矩阵乘法、`axis`、统计、累计、差分和排序 | [基础运算一](numpy和pandas学习/05_NumPy基础运算一.ipynb) · [基础运算二](numpy和pandas学习/06_NumPy基础运算二.ipynb) |
| 7～10 | 索引与遍历、数组合并、数组分割、复制与视图 | [索引与迭代](numpy和pandas学习/07_NumPy索引与迭代.ipynb) |
| 11～14 | `Series`、`DataFrame`、数据选择、设置值和缺失值处理 | [Pandas 基础](numpy和pandas学习/11_Pandas基础介绍.ipynb) · [处理缺失数据](numpy和pandas学习/14_Pandas处理缺失数据.ipynb) |
| 15 | CSV、Excel、Pickle 等数据导入导出 | [导入与导出](numpy和pandas学习/15_Pandas导入导出.ipynb) |
| 16～17 | `concat` 拼接与 `merge` 关联 | [concat](numpy和pandas学习/16_Pandas合并concat.ipynb) · [merge](numpy和pandas学习/17_Pandas合并merge.ipynb) |
| 18 | Pandas 折线图、散点图、柱状图和直方图 | [Pandas 绘图](numpy和pandas学习/18_Pandas绘图.ipynb) |

课程录制时间较早，因此笔记对部分旧写法做了更新：

- 使用 `loc`、`iloc` 代替已经移除的 `ix`。
- 使用 `pd.concat()` 代替已经移除的 `DataFrame.append()`。
- 避免链式赋值，统一使用 `df.loc[条件, 列名] = 新值`。

旧写法仍会在讲解中展示，方便看懂原视频，但不会放进需要连续运行的代码单元。

## 目录结构

```text
python_study/
├── python_course/              # Python 第 18～110、127～164 集
│   ├── 01_基础语法_类型转换与字符串/
│   ├── 02_布尔值与条件判断/
│   ├── 03_循环语句/
│   ├── 04_函数基础/
│   ├── 05_列表元组字符串集合字典/
│   ├── ...
│   └── 18_递归/
├── numpy和pandas学习/           # NumPy、Pandas 完整 18 集 Notebook
│   ├── 01_NumPy和Pandas有什么用.ipynb
│   ├── ...
│   └── 18_Pandas绘图.ipynb
├── python_class.ipynb          # 补充练习
├── .gitignore
└── README.md
```

## 开始使用

准备 Python 3.9 或更高版本，然后克隆仓库：

```bash
git clone https://github.com/lzynb0206/python-course-notes.git
cd python-course-notes
```

建议创建独立的虚拟环境：

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 运行 Python 示例

大部分 Python 基础章节只使用标准库，可以直接运行：

```bash
python3 "python_course/01_基础语法_类型转换与字符串/第18-28集_基础语法.py"
python3 "python_course/05_列表元组字符串集合字典/第62-80集_数据容器.py"
```

数据可视化章节需要额外安装依赖：

```bash
python3 -m pip install -r python_course/requirements.txt
```

MySQL 和 PySpark 属于可选内容，需要学习对应章节时再安装：

```bash
python3 -m pip install -r python_course/requirements-advanced.txt
```

### 打开 NumPy 与 Pandas Notebook

先安装 NumPy、Pandas、Matplotlib 和 JupyterLab：

```bash
python3 -m pip install -r "numpy和pandas学习/requirements.txt"
python3 -m jupyter lab
```

也可以直接用 PyCharm 打开 `.ipynb` 文件，并选择项目的 `.venv` 作为内核。Notebook 默认不保存预运行结果，建议从上到下逐格执行；每看完一个示例，可以修改数组形状、索引条件或表格数据，再观察结果如何变化。

## 运行时文件

- 文件操作和递归练习产生的数据放在各章节的 `runtime_data/`。
- Python 可视化示例生成的 HTML 放在对应章节的 `outputs/`。
- NumPy/Pandas 第 15、18 集生成的表格和图片放在 `numpy和pandas学习/runtime_data/`。
- 虚拟环境、运行结果、缓存和 IDE 配置均已加入 `.gitignore`。

SQL 示例默认只展示语句，不会主动连接或修改数据库；仓库中的疫情和 GDP 数据是用于演示处理流程的小型样例，不应作为现实统计数据使用。

## 当前进度

- Python 第 18～110 集：已整理
- Python 第 111～126 集：暂未整理
- Python 第 127～164 集：已整理
- NumPy 与 Pandas 第 1～18 集：已整理

## 课程来源

- [黑马程序员 Python 教程](https://www.bilibili.com/video/BV1qW4y1a7fU)
- [莫烦 Python：NumPy & Pandas 数据处理教程](https://www.bilibili.com/video/BV1Ex411L7oT)
- [莫烦 Python：NumPy & Pandas 图文教程](https://mofanpy.com/tutorials/data-manipulation/np-pd/)

本仓库仅用于个人学习与交流。课程版权归原作者所有。
