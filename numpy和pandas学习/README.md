# NumPy 和 Pandas 学习笔记

这套笔记对应莫烦 Python 的《Numpy & Pandas 数据处理教程》`BV1Ex411L7oT`，共 18 集。内容按照学习时的聊天记录重新整理，没有把原来逐项讲过的知识压缩成几段概括。

课程录制时间较早，核心概念仍然适用，但部分 Pandas 接口已经发生变化。这里使用当前常见写法重新整理，例如用 `loc`、`iloc` 代替已经移除的 `ix`，用 `pd.concat()` 代替 `DataFrame.append()`。因此可以按照原视频学习，也可以直接在较新的 NumPy 和 Pandas 环境中运行。

Notebook 是主要学习入口。每个小知识点都保留了具体说明、示例代码、预期输出和计算过程；课程中的旧接口会说明为什么不能再用，并给出新版 NumPy、Pandas 的对应写法。想连续复习整门课时，也可以阅读 [《18 集详细讲解》](18集详细讲解.md)。

## 笔记怎么组织

- 一集对应一个 Notebook，章节顺序与原聊天记录一致。
- Markdown 单元负责解释概念、参数、形状变化和结果为什么如此。
- 代码单元只放可以独立练习的示例；故意报错或已删除的旧写法留在 Markdown 中展示，不会打断“全部运行”。
- 第 13、14、17 集补了沿用自上一集的数据初始化，因此每本 Notebook 都能单独打开。
- 第 15、18 集产生的文件统一写入 `runtime_data/`，不会混进课程源文件。

## 课程目录

| 集数 | 视频主题 | Notebook |
|---:|---|---|
| 1 | NumPy 和 Pandas 有什么用 | [打开笔记](01_NumPy和Pandas有什么用.ipynb) |
| 2 | NumPy 和 Pandas 安装 | [打开笔记](02_安装与环境检查.ipynb) |
| 3 | NumPy 属性 | [打开笔记](03_NumPy数组属性.ipynb) |
| 4 | NumPy 创建 array | [打开笔记](04_NumPy创建数组.ipynb) |
| 5 | NumPy 基础运算 1 | [打开笔记](05_NumPy基础运算一.ipynb) |
| 6 | NumPy 基础运算 2 | [打开笔记](06_NumPy基础运算二.ipynb) |
| 7 | NumPy 索引 | [打开笔记](07_NumPy索引与迭代.ipynb) |
| 8 | NumPy array 合并 | [打开笔记](08_NumPy数组合并.ipynb) |
| 9 | NumPy array 分割 | [打开笔记](09_NumPy数组分割.ipynb) |
| 10 | NumPy copy 与 deep copy | [打开笔记](10_NumPy复制与视图.ipynb) |
| 11 | Pandas 基本介绍 | [打开笔记](11_Pandas基础介绍.ipynb) |
| 12 | Pandas 选择数据 | [打开笔记](12_Pandas选择数据.ipynb) |
| 13 | Pandas 设置值 | [打开笔记](13_Pandas设置值.ipynb) |
| 14 | Pandas 处理丢失数据 | [打开笔记](14_Pandas处理缺失数据.ipynb) |
| 15 | Pandas 导入导出 | [打开笔记](15_Pandas导入导出.ipynb) |
| 16 | Pandas 合并 concat | [打开笔记](16_Pandas合并concat.ipynb) |
| 17 | Pandas 合并 merge | [打开笔记](17_Pandas合并merge.ipynb) |
| 18 | Pandas plot 画图 | [打开笔记](18_Pandas绘图.ipynb) |

## 安装

建议使用 Python 3.9 或更高版本，并在仓库的虚拟环境中安装依赖：

```bash
python3 -m pip install -r "numpy和pandas学习/requirements.txt"
```

如果使用仓库已有的 `.venv`：

```bash
.venv/bin/python -m pip install -r "numpy和pandas学习/requirements.txt"
```

## 打开并学习

用 PyCharm 打开任意 `.ipynb` 文件，选择项目的 `.venv` 作为 Python 内核，然后从上到下逐格运行即可。

也可以在终端启动 JupyterLab：

```bash
.venv/bin/python -m jupyter lab
```

推荐按编号顺序学习。读完一个 Markdown 说明后，先猜一猜下一格代码的结果，再运行验证；随后修改数组形状、筛选条件或表格内容，看看结果如何变化。

Notebook 默认不保存预运行结果，第一次打开时需要自己执行代码单元。这样更适合动手学习，也能避免不同版本产生的旧输出干扰。

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
