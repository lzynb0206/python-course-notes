"""
第 108～110 集：柱状图、时间线和动态 GDP 柱状图。

data/gdp_demo.csv 是缩小版练习数据，用于演示课程中的处理流程。
数值仅供编程练习，不应当作为现实统计结论使用。
"""

from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "gdp_demo.csv"
OUTPUT_DIR = BASE_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)


def show_title(title):
    print(f"\n{'=' * 12} {title} {'=' * 12}")


def load_pyecharts():
    try:
        from pyecharts.charts import Bar, Timeline
        from pyecharts.globals import ThemeType
        from pyecharts.options import InitOpts, LabelOpts, TitleOpts
    except ModuleNotFoundError:
        return None
    return Bar, Timeline, ThemeType, InitOpts, LabelOpts, TitleOpts


show_title("1. 第 108 集：基础柱状图的知识结构")

print("Bar() -> add_xaxis() -> add_yaxis() -> reversal_axis() -> render()")
print("reversal_axis() 会交换横纵轴，LabelOpts(position='right') 把数值放到右侧。")


show_title("2. 第 109 集：排序是动态排名图的准备知识")

my_list = [["a", 33], ["b", 55], ["c", 11]]

# key 接收函数：每次把一个小列表交给 Lambda，并用下标 1 的数值作为排序依据。
my_list.sort(key=lambda element: element[1], reverse=True)
print(my_list)                            # [['b', 55], ['a', 33], ['c', 11]]

# reverse=True 代表从大到小。
# sort() 修改原列表；sorted() 返回新列表。这与第 79 集知识形成衔接。


show_title("3. 第 110 集：读取并整理 GDP 数据")

# 原课程数据文件使用 GB2312 编码；这个练习文件保存为 UTF-8，因此这里使用 utf-8。
with open(DATA_FILE, "r", encoding="utf-8") as file:
    data_lines = file.readlines()

# 第一行是表头 year,country,gdp，不是正式数据，所以删除。
data_lines.pop(0)

# 目标结构：
# {
#     2020: [["中国", 147227.0], ["美国", 209366.0], ...],
#     2021: [...],
# }
data_dict = {}

for line in data_lines:
    clean_line = line.strip()
    # 文件末尾可能存在空行；空行没有三列数据，应先跳过。
    if not clean_line:
        continue

    year_text, country, gdp_text = clean_line.split(",")
    year = int(year_text)
    gdp = float(gdp_text)

    # 课程使用 try/except KeyError 判断年份是否首次出现，复习第 91～93 集。
    try:
        data_dict[year].append([country, gdp])
    except KeyError:
        data_dict[year] = []
        data_dict[year].append([country, gdp])

print("所有年份：", sorted(data_dict.keys()))
print("2020 年前两条原始数据：", data_dict[2020][:2])


def render_charts():
    pyecharts_items = load_pyecharts()
    if pyecharts_items is None:
        print("\n没有检测到 pyecharts，已跳过 HTML 图表生成。")
        print("安装命令：python3 -m pip install pyecharts")
        return

    Bar, Timeline, ThemeType, InitOpts, LabelOpts, TitleOpts = pyecharts_items

    show_title("4. 生成第 108 集基础柱状图")

    basic_bar = Bar()
    basic_bar.add_xaxis(["中国", "美国", "英国"])
    basic_bar.add_yaxis(
        "GDP",
        [30, 20, 10],
        label_opts=LabelOpts(position="right"),
    )
    basic_bar.reversal_axis()
    basic_output = OUTPUT_DIR / "07_basic_bar.html"
    basic_bar.render(str(basic_output))
    print("基础柱状图：", basic_output)

    show_title("5. 生成第 109 集基础时间线柱状图")

    timeline = Timeline(init_opts=InitOpts(theme=ThemeType.LIGHT))
    timeline_demo_data = {
        "2020": [30, 20, 10],
        "2021": [50, 40, 20],
        "2022": [70, 60, 30],
    }

    for year, values in timeline_demo_data.items():
        bar = Bar()
        bar.add_xaxis(["中国", "美国", "英国"])
        bar.add_yaxis("GDP", values, label_opts=LabelOpts(position="right"))
        bar.reversal_axis()
        timeline.add(bar, f"{year}年")

    timeline.add_schema(
        play_interval=1000,       # 每隔 1000 毫秒切换一次
        is_timeline_show=True,    # 显示下方时间线
        is_auto_play=True,        # 打开页面后自动播放
        is_loop_play=True,        # 播放结束后循环
    )
    timeline_output = OUTPUT_DIR / "07_basic_timeline_bar.html"
    timeline.render(str(timeline_output))
    print("基础时间线：", timeline_output)

    show_title("6. 生成第 110 集动态 GDP 柱状图")

    gdp_timeline = Timeline(init_opts=InitOpts(theme=ThemeType.LIGHT))
    sorted_year_list = sorted(data_dict.keys())

    for year in sorted_year_list:
        # 每一年内部按 GDP 从高到低排序，只取前 8 名。
        data_dict[year].sort(key=lambda element: element[1], reverse=True)
        year_data = data_dict[year][0:8]

        x_data = []
        y_data = []
        for country_gdp in year_data:
            x_data.append(country_gdp[0])
            y_data.append(country_gdp[1])

        # 横向柱状图从下往上排列；反转后，最大值会显示在最上方。
        x_data.reverse()
        y_data.reverse()

        bar = Bar()
        bar.add_xaxis(x_data)
        bar.add_yaxis(
            "GDP（亿美元，教学数据）",
            y_data,
            label_opts=LabelOpts(position="right"),
        )
        bar.reversal_axis()
        bar.set_global_opts(
            title_opts=TitleOpts(title=f"{year} 年全球 GDP 前 8 名（教学数据）")
        )
        gdp_timeline.add(bar, str(year))

    gdp_timeline.add_schema(
        play_interval=1000,
        is_timeline_show=True,
        is_auto_play=True,
        is_loop_play=False,
    )
    gdp_output = OUTPUT_DIR / "07_dynamic_gdp_top8.html"
    gdp_timeline.render(str(gdp_output))
    print("动态 GDP 柱状图：", gdp_output)


render_charts()

print("\n第 110 集知识链：读取 CSV -> 按年份分组 -> 排序取前 8 -> 每年创建 Bar -> 加入 Timeline。")
