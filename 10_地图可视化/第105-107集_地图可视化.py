"""
第 105～107 集：pyecharts 地图可视化。

包含：
1. 基础中国地图。
2. 从嵌套疫情数据中提取省份，绘制全国疫情地图。
3. 从河南数据中提取城市，绘制河南省疫情地图。

内置数值只是用于练习数据结构和绘图，不代表真实疫情数据。
"""

from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)


def show_title(title):
    print(f"\n{'=' * 12} {title} {'=' * 12}")


# 缩小版数据保留了课程所用的 areaTree -> 中国 -> 省份 -> 城市结构。
epidemic_data = {
    "areaTree": [
        {
            "name": "中国",
            "children": [
                {
                    "name": "北京",
                    "total": {"confirm": 1200},
                    "children": [],
                },
                {
                    "name": "上海",
                    "total": {"confirm": 1800},
                    "children": [],
                },
                {
                    "name": "广东",
                    "total": {"confirm": 2500},
                    "children": [],
                },
                {
                    "name": "河南",
                    "total": {"confirm": 1500},
                    "children": [
                        {"name": "郑州", "total": {"confirm": 600}},
                        {"name": "开封", "total": {"confirm": 120}},
                        {"name": "洛阳", "total": {"confirm": 200}},
                        {"name": "安阳", "total": {"confirm": 80}},
                    ],
                },
                {
                    "name": "湖北",
                    "total": {"confirm": 68000},
                    "children": [],
                },
            ],
        }
    ]
}


def load_pyecharts():
    """延迟导入，让没安装 pyecharts 时仍能学习数据提取部分。"""
    try:
        from pyecharts.charts import Map
        from pyecharts.options import TitleOpts, VisualMapOpts
    except ModuleNotFoundError:
        return None
    return Map, TitleOpts, VisualMapOpts


def visual_pieces():
    """VisualMapOpts 使用的分段颜色配置。"""
    return [
        {"min": 1, "max": 99, "label": "1～99人", "color": "#CCFFFF"},
        {"min": 100, "max": 999, "label": "100～999人", "color": "#FFFF99"},
        {"min": 1000, "max": 9999, "label": "1000～9999人", "color": "#FF9966"},
        {"min": 10000, "label": "10000人以上", "color": "#990033"},
    ]


show_title("1. 第 105 集：地图要求的数据形式")

basic_data = [
    ("北京市", 99),
    ("上海市", 199),
    ("广东省", 299),
    ("河南省", 399),
]
print(basic_data)

# 地图数据必须是 [(地区名称, 数值), ...]。
# 地区名必须与地图中的标准名称匹配，否则对应区域不会着色。


show_title("2. 第 106 集：提取全国各省数据")

province_data_list = epidemic_data["areaTree"][0]["children"]
province_map_data = []

for province_data in province_data_list:
    province_name = province_data["name"]
    province_confirm = province_data["total"]["confirm"]
    province_map_data.append((province_name, province_confirm))

print(province_map_data)


show_title("3. 第 107 集：提取河南各城市数据")

# 原课程固定使用 children[3] 取得河南，这依赖省份顺序。
# 更稳妥的做法是按 name 查找。
henan_data = None
for province_data in province_data_list:
    if province_data["name"] == "河南":
        henan_data = province_data
        break

if henan_data is None:
    raise ValueError("数据中没有找到河南省")

city_map_data = []
for city_data in henan_data["children"]:
    city_name = city_data["name"]

    # pyecharts 河南地图一般使用“郑州市”这类标准名称。
    if not city_name.endswith("市"):
        city_name += "市"

    city_confirm = city_data["total"]["confirm"]
    city_map_data.append((city_name, city_confirm))

# 课程数据中济源市不在普通城市 children 中，因此手动补充。
if not any(city_name == "济源市" for city_name, _ in city_map_data):
    city_map_data.append(("济源市", 5))

print(city_map_data)


def render_maps():
    pyecharts_items = load_pyecharts()
    if pyecharts_items is None:
        print("\n没有检测到 pyecharts，已跳过 HTML 地图生成。")
        print("安装命令：python3 -m pip install pyecharts")
        return

    Map, TitleOpts, VisualMapOpts = pyecharts_items

    # 第 105 集：基础地图。
    basic_map = Map()
    basic_map.add("演示数据", basic_data, "china")
    basic_map.set_global_opts(
        title_opts=TitleOpts(title="全国基础地图"),
        visualmap_opts=VisualMapOpts(is_show=True, is_piecewise=True, pieces=visual_pieces()),
    )
    basic_output = OUTPUT_DIR / "06_basic_china_map.html"
    basic_map.render(str(basic_output))

    # 第 106 集：全国各省疫情地图。
    china_map = Map()
    china_map.add("各省确诊人数", province_map_data, "china")
    china_map.set_global_opts(
        title_opts=TitleOpts(title="全国疫情地图（教学数据）"),
        visualmap_opts=VisualMapOpts(is_show=True, is_piecewise=True, pieces=visual_pieces()),
    )
    china_output = OUTPUT_DIR / "06_china_epidemic_map.html"
    china_map.render(str(china_output))

    # 第 107 集：河南各城市疫情地图。
    henan_map = Map()
    henan_map.add("河南各城市确诊人数", city_map_data, "河南")
    henan_map.set_global_opts(
        title_opts=TitleOpts(title="河南省疫情地图（教学数据）"),
        visualmap_opts=VisualMapOpts(is_show=True, is_piecewise=True, pieces=visual_pieces()),
    )
    henan_output = OUTPUT_DIR / "06_henan_epidemic_map.html"
    henan_map.render(str(henan_output))

    print("地图已生成：")
    print(basic_output)
    print(china_output)
    print(henan_output)


show_title("4. 生成地图")
render_maps()

print("\n横向关系：全国地图提取中国下面的省；河南地图继续提取河南下面的市。")

