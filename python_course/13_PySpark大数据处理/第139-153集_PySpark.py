"""
第 139～153 集：PySpark 大数据处理。

前半部分用普通 Python 模拟 RDD 转换，未安装 Spark 也能直接运行并理解逻辑。
文件末尾保留真实 PySpark 示例；准备好 Java 与 PySpark 后，将
RUN_REAL_PYSPARK_DEMO 改为 True 即可运行。
"""

import json
from collections import defaultdict
from pathlib import Path


RUN_REAL_PYSPARK_DEMO = False


def show_title(title):
    print(f"\n{'=' * 12} {title} {'=' * 12}")


show_title("1. 第 139～141 集：PySpark 与数据输入")

# Spark 是分布式计算框架；PySpark 是它的 Python 接口。
# RDD（弹性分布式数据集）可以理解为“分散在多个计算节点上的数据集合”。
#
# 常见创建方式：
# sc.parallelize([1, 2, 3])       把 Python 容器并行化
# sc.textFile("input.txt")       从文本文件读取，每一行成为一个元素
#
# 转换算子（Transformation）通常是惰性的：先记录计算步骤。
# 行动算子（Action）才触发真正计算，例如 collect、count、take。
numbers = [1, 2, 3, 4, 5]
print("模拟 parallelize 输入：", numbers)


show_title("2. 第 142 集：map")

# map：一进一出，对每个元素执行同一个函数。
mapped = list(map(lambda number: number * 10, numbers))
print("每个数字乘 10：", mapped)


show_title("3. 第 143 集：flatMap")

# map 会保留每次返回的容器；flatMap 会再把这些容器压平一层。
sentences = ["hello python", "hello spark"]
map_result = [sentence.split() for sentence in sentences]
flat_map_result = [word for sentence in sentences for word in sentence.split()]
print("map 结果：", map_result)
print("flatMap 结果：", flat_map_result)


show_title("4. 第 144 集：reduceByKey")

# reduceByKey 处理 (key, value) 二元组，把相同 key 的 value 聚合。
word_pairs = [(word, 1) for word in flat_map_result]
word_count = defaultdict(int)
for word, count in word_pairs:
    word_count[word] += count
print("词频统计：", dict(word_count))


show_title("5. 第 145 集：练习——单词计数")

text_lines = [
    "itheima python spark",
    "python spark",
    "python",
]
words = [word for line in text_lines for word in line.split()]
counts = defaultdict(int)
for word in words:
    counts[word] += 1
print("练习结果：", dict(counts))


show_title("6. 第 146～148 集：filter、distinct、sortBy")

# filter：只保留条件为 True 的元素。
filtered = [number for number in numbers if number % 2 == 0]

# distinct：去重。RDD 不保证结果顺序；普通 Python 示例用 dict 保留首次顺序。
duplicated = [1, 1, 2, 3, 3, 4]
distinct_numbers = list(dict.fromkeys(duplicated))

# sortBy：根据指定规则排序。ascending=False 表示降序。
scores = [("小明", 88), ("小红", 95), ("小刚", 76)]
sorted_scores = sorted(scores, key=lambda item: item[1], reverse=True)

print("filter 偶数：", filtered)
print("distinct 去重：", distinct_numbers)
print("sortBy 按成绩降序：", sorted_scores)


show_title("7. 第 149 集：练习——城市销售额排行")

sales = [
    ("北京", 100),
    ("上海", 80),
    ("北京", 120),
    ("广州", 90),
    ("上海", 70),
]
city_totals = defaultdict(int)
for city, amount in sales:
    city_totals[city] += amount
ranking = sorted(city_totals.items(), key=lambda item: item[1], reverse=True)
print("城市销售额：", ranking)


show_title("8. 第 150～151 集：输出算子")

# 转为 Python 对象（行动算子）：
# collect()  全部收集到驱动程序；数据很大时可能耗尽内存
# take(n)    只取前 n 个元素，适合查看样本
# count()    统计元素数量
# first()    取第一个元素
#
# 输出到文件：saveAsTextFile("目录")。Spark 会按分区生成 part-* 文件，
# 参数是“输出目录”而不是单个文件，并且该目录通常不能事先存在。
print("collect 模拟：", ranking)
print("take(2) 模拟：", ranking[:2])
print("count 模拟：", len(ranking))


show_title("9. 第 152 集：综合案例——JSON 订单统计")

order_lines = [
    '{"area": "北京", "category": "图书", "money": 40}',
    '{"area": "上海", "category": "文具", "money": 20}',
    '{"area": "北京", "category": "文具", "money": 30}',
    '{"area": "广州", "category": "图书", "money": 50}',
]

# 对应 Spark 流程：map(JSON 解析) -> map(组成键值对)
# -> reduceByKey(聚合) -> sortBy(排行) -> collect(取回结果)。
orders = [json.loads(line) for line in order_lines]
area_amounts = defaultdict(float)
for order in orders:
    area_amounts[order["area"]] += float(order["money"])
area_ranking = sorted(area_amounts.items(), key=lambda item: item[1], reverse=True)
print("地区销售额排行：", area_ranking)


show_title("10. 第 153 集：真实 PySpark 与分布式提交")


def run_real_pyspark_demo():
    """用真实 RDD 重做本章核心算子。"""
    try:
        from pyspark import SparkConf, SparkContext
    except ImportError:
        print("尚未安装 PySpark：python3 -m pip install pyspark")
        return

    conf = SparkConf().setAppName("python-course-demo").setMaster("local[*]")
    context = SparkContext.getOrCreate(conf=conf)
    context.setLogLevel("ERROR")

    try:
        rdd = context.parallelize(order_lines)
        result = (
            rdd.map(json.loads)
            .map(lambda order: (order["area"], float(order["money"])))
            .reduceByKey(lambda left, right: left + right)
            .filter(lambda item: item[1] >= 40)
            .sortBy(lambda item: item[1], ascending=False)
        )
        print("真实 PySpark collect：", result.collect())
        print("真实 PySpark take(2)：", result.take(2))

        output_dir = Path(__file__).resolve().parent / "runtime_data" / "spark_output"
        if output_dir.exists():
            print("输出目录已存在，为避免覆盖，本次跳过 saveAsTextFile：", output_dir)
        else:
            result.saveAsTextFile(str(output_dir))
            print("Spark 分区文件已输出到：", output_dir)
    finally:
        context.stop()


if RUN_REAL_PYSPARK_DEMO:
    run_real_pyspark_demo()
else:
    print("真实 PySpark 演示默认关闭；其余纯 Python 示例已正常运行。")

# 本地学习常用 .setMaster("local[*]")；提交到集群时通常不把 master 写死在代码中，
# 而是交给 spark-submit 参数和集群管理器配置：
# spark-submit --master yarn 第139-153集_PySpark.py


show_title("11. 常用算子横向比较")

operator_comparison = [
    ("map", "一个元素变成一个元素", "转换"),
    ("flatMap", "一个元素可展开为多个元素", "转换"),
    ("filter", "按条件保留元素", "转换"),
    ("distinct", "去重", "转换"),
    ("reduceByKey", "按键聚合值", "转换"),
    ("sortBy", "按规则排序", "转换"),
    ("collect/take/count", "得到结果并触发计算", "行动"),
    ("saveAsTextFile", "把各分区写入目录", "行动"),
]
for name, purpose, operator_type in operator_comparison:
    print(f"{name:<20} | {operator_type:<2} | {purpose}")
