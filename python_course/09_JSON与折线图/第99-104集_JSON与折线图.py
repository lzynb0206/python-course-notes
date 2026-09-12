"""
第 99～104 集：JSON 数据与 pyecharts 折线图。

课程主线：
案例介绍 -> JSON 转换 -> 认识 pyecharts -> 基础折线图
-> 清洗三个国家的 JSONP 数据 -> 生成疫情趋势折线图

本文件使用少量内置演示数据复现相同结构，不依赖课程的大型数据文件。
"""

import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)


def show_title(title):
    print(f"\n{'=' * 12} {title} {'=' * 12}")


show_title("1. 第 99～100 集：Python 数据与 JSON")

python_data = {
    "name": "黑马程序员",
    "students": 100,
    "is_open": True,
    "remark": None,
    "courses": ["Python", "大数据"],
}

# json.dumps：Python 数据 -> JSON 字符串。
# ensure_ascii=False：让中文直接显示，而不是显示为 \uXXXX。
json_text = json.dumps(python_data, ensure_ascii=False)
print("JSON 字符串：", json_text)
print("转换后类型：", type(json_text))      # <class 'str'>

# json.loads：JSON 字符串 -> Python 数据。
restored_data = json.loads(json_text)
print("还原后的 Python 数据：", restored_data)
print("还原后类型：", type(restored_data))  # <class 'dict'>

# 类型对应关系：
# JSON object  <-> Python dict
# JSON array   <-> Python list
# JSON string  <-> Python str
# JSON number  <-> Python int / float
# JSON true/false/null <-> Python True/False/None


show_title("2. 第 103 集：JSONP 数据为什么不能直接 loads")


def make_country_jsonp(callback_name, dates, values):
    """构造与课程数据结构相似的缩小版 JSONP 字符串。"""
    payload = {
        "data": [
            {
                "trend": {
                    "updateDate": dates,
                    "list": [{"name": "确诊", "data": values}],
                }
            }
        ]
    }
    return f"{callback_name}({json.dumps(payload, ensure_ascii=False)});"


def parse_jsonp(jsonp_text):
    """去掉 callback_name( 和末尾 );，再把中间的 JSON 转成字典。"""
    left_parenthesis = jsonp_text.find("(")
    right_parenthesis = jsonp_text.rfind(")")

    if left_parenthesis == -1 or right_parenthesis == -1:
        raise ValueError("这段文本不是预期的 JSONP 格式")

    json_part = jsonp_text[left_parenthesis + 1:right_parenthesis]
    return json.loads(json_part)


dates = ["2020-01", "2020-02", "2020-03", "2020-04", "2020-05"]
usa_text = make_country_jsonp("jsonp_usa", dates, [5, 30, 120, 260, 400])
japan_text = make_country_jsonp("jsonp_japan", dates, [2, 15, 45, 90, 150])
india_text = make_country_jsonp("jsonp_india", dates, [1, 8, 60, 180, 350])

print("JSONP 开头示例：", usa_text[:45] + "...")

# 原课程使用固定切片去掉每个文件不同的回调函数前缀。
# 这里用 find/rfind 寻找括号，更不容易因回调名称长度改变而出错。
usa_dict = parse_jsonp(usa_text)
japan_dict = parse_jsonp(japan_text)
india_dict = parse_jsonp(india_text)


show_title("3. 逐层提取日期和确诊人数")

usa_trend = usa_dict["data"][0]["trend"]
japan_trend = japan_dict["data"][0]["trend"]
india_trend = india_dict["data"][0]["trend"]

x_data = usa_trend["updateDate"]
usa_y_data = usa_trend["list"][0]["data"]
japan_y_data = japan_trend["list"][0]["data"]
india_y_data = india_trend["list"][0]["data"]

print("横轴日期：", x_data)
print("美国数据：", usa_y_data)
print("日本数据：", japan_y_data)
print("印度数据：", india_y_data)

# 一条折线要求横轴和纵轴数量相同，否则数据会错位。
assert len(x_data) == len(usa_y_data) == len(japan_y_data) == len(india_y_data)


def render_line_chart():
    """第 101、102、104 集：创建并渲染折线图。"""
    try:
        from pyecharts.charts import Line
        from pyecharts.options import LabelOpts, LegendOpts, TitleOpts, ToolboxOpts
    except ModuleNotFoundError:
        print("\n没有检测到 pyecharts，已跳过 HTML 图表生成。")
        print("安装命令：python3 -m pip install pyecharts")
        return

    line = Line()
    line.add_xaxis(x_data)

    # label_opts=LabelOpts(is_show=False) 隐藏每个数据点旁边的数字，避免拥挤。
    line.add_yaxis(
        "美国确诊人数",
        usa_y_data,
        label_opts=LabelOpts(is_show=False),
    )
    line.add_yaxis(
        "日本确诊人数",
        japan_y_data,
        label_opts=LabelOpts(is_show=False),
    )
    line.add_yaxis(
        "印度确诊人数",
        india_y_data,
        label_opts=LabelOpts(is_show=False),
    )

    # set_global_opts 配置整张图；add_yaxis 中的 label_opts 配置具体系列。
    line.set_global_opts(
        title_opts=TitleOpts(title="美日印三国疫情确诊人数对比", pos_left="center"),
        legend_opts=LegendOpts(is_show=True),
        toolbox_opts=ToolboxOpts(is_show=True),
    )

    output_path = OUTPUT_DIR / "05_covid_line_chart.html"
    line.render(str(output_path))
    print("折线图已生成：", output_path)


show_title("4. 第 101～104 集：生成折线图")
render_line_chart()

