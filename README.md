# Python Study

这是我的 Python 学习仓库，用于保存课程笔记、Jupyter Notebook、示例代码和练习项目。

当前主要学习内容来自黑马程序员 Python 入门课程 `BV1qW4y1a7fU`，已经把第 **18～110 集**及第 **127～164 集**按照知识章节整理成可直接运行的 Python 文件。

## 仓库结构

```text
python_study/
├── python_class.ipynb     # 日常 Jupyter Notebook 学习记录
├── python_course/         # 第 18～110、127～164 集课程分类代码
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
├── .gitignore
└── README.md
```

课程文件的详细集数、知识点和运行方式，请查看 [python_course/README.md](python_course/README.md)。

## 运行环境

- Python 3.9 或更高版本
- Jupyter Notebook（运行 `.ipynb` 文件时需要）
- pyecharts（运行第 101～110 集可视化案例时需要）
- PyMySQL（运行第 136～138 集真实数据库案例时可选）
- PySpark 与 Java（运行第 139～153 集真实 Spark 案例时可选）

安装课程可视化依赖：

```bash
python3 -m pip install -r python_course/requirements.txt
```

如需连接 MySQL 或运行真实 PySpark，再安装进阶依赖：

```bash
python3 -m pip install -r python_course/requirements-advanced.txt
```

## 运行课程代码

在仓库根目录执行：

```bash
python3 "python_course/01_基础语法_类型转换与字符串/第18-28集_基础语法.py"
python3 "python_course/05_列表元组字符串集合字典/第62-80集_数据容器.py"
python3 "python_course/11_柱状图与时间线/第108-110集_柱状图与时间线.py"
python3 "python_course/14_闭包装饰器与设计模式/第154-157集_高级语法与设计模式.py"
python3 "python_course/18_递归/第164集_递归.py"
```

## 学习范围

| 集数 | 知识模块 |
|---:|---|
| 18～28 | 类型转换、运算符、字符串格式化与输入 |
| 29～37 | 布尔值与条件判断 |
| 38～50 | while、for、range、循环控制 |
| 51～61 | 函数基础、参数、返回值与作用域 |
| 62～80 | 列表、元组、字符串、集合、字典 |
| 81～84 | 函数进阶、`*args`、`**kwargs`、Lambda |
| 85～90 | 文件读取、写入、追加与综合案例 |
| 91～98 | 异常、模块、自定义包与第三方包 |
| 99～104 | JSON、数据清洗与折线图 |
| 105～107 | 地图可视化 |
| 108～110 | 柱状图、时间线与动态 GDP 图 |
| 127～138 | SQL、MySQL 与 Python 数据库操作 |
| 139～153 | PySpark RDD、常用算子、输出与综合案例 |
| 154～157 | 闭包、装饰器、单例模式与工厂模式 |
| 158～159 | 多线程概念、创建线程与线程同步 |
| 160～161 | Socket 服务端与客户端 |
| 162～163 | 正则表达式基础与元字符 |
| 164 | 递归 |

## 说明

- `.venv/` 是本机虚拟环境，体积较大且不可移植，因此不提交。
- `.idea/` 是 PyCharm 本机项目配置，不提交。
- `runtime_data/`、`outputs/*.html` 是运行案例后生成的临时文件，不提交。
- 疫情和 GDP 示例使用缩小版教学数据，只用于练习代码，不作为现实统计依据。
- 本次按指定范围从第 127 集继续，因此第 111～126 集暂未收录。

## 课程来源

- <https://www.bilibili.com/video/BV1qW4y1a7fU>
