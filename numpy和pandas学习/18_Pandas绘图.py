"""第 18 集：使用 Pandas 的 plot 接口快速绘图。"""

from pathlib import Path

import matplotlib

# 使用非交互后端，脚本在终端和无图形界面的环境中都能运行。
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


base_dir = Path(__file__).resolve().parent
output_dir = base_dir / "runtime_data"
output_dir.mkdir(exist_ok=True)
output_file = output_dir / "pandas_plot.png"

rng = np.random.default_rng(seed=42)


print("1. Series 折线图")
series = pd.Series(rng.normal(size=100), name="random_walk").cumsum()


print("2. DataFrame 多列折线图")
frame = pd.DataFrame(
    rng.normal(size=(100, 4)),
    columns=list("ABCD"),
).cumsum()


print("3. 柱状图和散点图")
summary = pd.Series({"Python": 88, "SQL": 92, "Pandas": 85})

fig, axes = plt.subplots(2, 2, figsize=(12, 8))

series.plot(ax=axes[0, 0], title="Series - Random Walk", color="steelblue")
axes[0, 0].set_xlabel("step")
axes[0, 0].set_ylabel("value")

frame.plot(ax=axes[0, 1], title="DataFrame - Multiple Lines")
axes[0, 1].set_xlabel("step")

summary.plot.bar(ax=axes[1, 0], title="Scores", color=["#4C72B0", "#55A868", "#C44E52"])
axes[1, 0].set_ylabel("score")
axes[1, 0].tick_params(axis="x", rotation=0)

frame.plot.scatter(
    x="A",
    y="B",
    c="C",
    colormap="viridis",
    ax=axes[1, 1],
    title="A vs B (color = C)",
)

fig.tight_layout()
fig.savefig(output_file, dpi=150)
plt.close(fig)
print("图片已保存：", output_file)

# 在有图形界面的本机环境中，也可以去掉 Agg 设置并使用 plt.show() 打开窗口。
#
# 常见 kind：
# line    折线图，观察趋势
# bar     柱状图，比较类别
# hist    直方图，观察数值分布
# box     箱线图，观察中位数与异常值
# area    面积图
# scatter 散点图，观察两个变量的关系
# pie     饼图，展示简单占比
#
# Pandas 绘图适合快速探索数据；需要精细控制布局和样式时，可以继续使用返回的
# Matplotlib Axes 对象设置标题、坐标轴、图例和标注。
