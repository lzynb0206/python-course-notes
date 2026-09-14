# NumPy 和 Pandas 学习笔记

这组代码对应莫烦 Python 的《Numpy & Pandas 数据处理教程》`BV1Ex411L7oT`，共 18 集。

课程录制时间较早，核心概念仍然适用，但部分 Pandas 接口已经发生变化。这里使用当前常见写法重新整理，例如用 `loc`、`iloc` 代替已经移除的 `ix`，用 `pd.concat()` 代替 `DataFrame.append()`。因此可以按照原视频学习，也可以直接在较新的 NumPy 和 Pandas 环境中运行。

建议先阅读 [《18 集详细讲解》](18集详细讲解.md)，再打开对应的 Python 文件动手运行。讲义负责解释概念、使用场景和易错点，代码中的少量输出只用来验证运算结果。

## 课程目录

| 集数 | 视频主题 | 对应代码 |
|---:|---|---|
| 1 | NumPy 和 Pandas 有什么用 | `01_NumPy和Pandas有什么用.py` |
| 2 | NumPy 和 Pandas 安装 | `02_安装与环境检查.py` |
| 3 | NumPy 属性 | `03_NumPy数组属性.py` |
| 4 | NumPy 创建 array | `04_NumPy创建数组.py` |
| 5 | NumPy 基础运算 1 | `05_NumPy基础运算一.py` |
| 6 | NumPy 基础运算 2 | `06_NumPy基础运算二.py` |
| 7 | NumPy 索引 | `07_NumPy索引与迭代.py` |
| 8 | NumPy array 合并 | `08_NumPy数组合并.py` |
| 9 | NumPy array 分割 | `09_NumPy数组分割.py` |
| 10 | NumPy copy 与 deep copy | `10_NumPy复制与视图.py` |
| 11 | Pandas 基本介绍 | `11_Pandas基础介绍.py` |
| 12 | Pandas 选择数据 | `12_Pandas选择数据.py` |
| 13 | Pandas 设置值 | `13_Pandas设置值.py` |
| 14 | Pandas 处理丢失数据 | `14_Pandas处理缺失数据.py` |
| 15 | Pandas 导入导出 | `15_Pandas导入导出.py` |
| 16 | Pandas 合并 concat | `16_Pandas合并concat.py` |
| 17 | Pandas 合并 merge | `17_Pandas合并merge.py` |
| 18 | Pandas plot 画图 | `18_Pandas绘图.py` |

## 安装

建议使用 Python 3.9 或更高版本，并在仓库的虚拟环境中安装依赖：

```bash
python3 -m pip install -r "numpy和pandas学习/requirements.txt"
```

如果使用仓库已有的 `.venv`：

```bash
.venv/bin/python -m pip install -r "numpy和pandas学习/requirements.txt"
```

## 运行

每个文件都可以单独执行。例如：

```bash
.venv/bin/python "numpy和pandas学习/03_NumPy数组属性.py"
.venv/bin/python "numpy和pandas学习/12_Pandas选择数据.py"
.venv/bin/python "numpy和pandas学习/18_Pandas绘图.py"
```

推荐按编号顺序学习。先阅读每一节的注释，尝试判断输出，再运行代码并修改数组形状、索引条件或表格内容观察结果。

## 几个容易混淆的概念

| 概念 | 区别 |
|---|---|
| `axis=0` / `axis=1` | 对二维表来说，`axis=0` 沿行方向计算并为每列产生结果；`axis=1` 沿列方向计算并为每行产生结果 |
| `*` / `@` | NumPy 中 `*` 是对应元素相乘，`@` 是矩阵乘法 |
| 切片 / `copy()` | NumPy 基础切片通常共享原数据；`copy()` 创建独立副本 |
| `loc` / `iloc` | `loc` 使用行列标签，`iloc` 使用整数位置 |
| `concat` / `merge` | `concat` 沿某个轴拼接，`merge` 根据键关联两张表 |
| `NaN` / `None` | 都可能表示缺失；Pandas 会根据列的数据类型选择具体的缺失值表示 |

第 15 集生成的文件和第 18 集生成的图片会放进本目录的 `runtime_data/`，该目录不会提交到 Git。

## 参考资料

- [Bilibili 课程](https://www.bilibili.com/video/BV1Ex411L7oT)
- [莫烦 Python 图文教程](https://mofanpy.com/tutorials/data-manipulation/np-pd/)
- [NumPy 用户指南](https://numpy.org/doc/stable/user/)
- [Pandas 用户指南](https://pandas.pydata.org/docs/user_guide/)

本目录是配合课程整理的学习笔记，课程内容版权归原作者所有。
