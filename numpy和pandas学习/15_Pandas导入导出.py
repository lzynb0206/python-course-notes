"""第 15 集：用 Pandas 读取和保存 CSV、Pickle、JSON。"""

from pathlib import Path

import pandas as pd


base_dir = Path(__file__).resolve().parent
input_file = base_dir / "student.csv"
output_dir = base_dir / "runtime_data"
output_dir.mkdir(exist_ok=True)


print("1. 读取 CSV")
students = pd.read_csv(input_file)
print(students)
print("\n字段类型：\n", students.dtypes)

# 常用参数：
# sep=","              字段分隔符
# encoding="utf-8"     文件编码
# usecols=[...]         只读取需要的列
# dtype={...}           指定列类型
# na_values=[...]       把指定文字识别为缺失值
# parse_dates=[...]     把指定列解析为日期


print("\n2. 清理后导出 CSV")
cleaned = students.dropna(subset=["score"]).copy()
cleaned["score"] = cleaned["score"].astype("int64")
csv_output = output_dir / "students_cleaned.csv"
cleaned.to_csv(csv_output, index=False, encoding="utf-8")
print("已保存：", csv_output)
print(pd.read_csv(csv_output))

# index=False 避免把 DataFrame 行索引额外写成一列。


print("\n3. Pickle：保留 Python/Pandas 数据类型")
pickle_output = output_dir / "students.pkl"
cleaned.to_pickle(pickle_output)
restored = pd.read_pickle(pickle_output)
print("还原后与原表相同：", restored.equals(cleaned))

# Pickle 适合可信环境中的 Python 临时数据交换，不应读取来源不明的 pickle 文件。


print("\n4. JSON：方便与其他语言或接口交换")
json_output = output_dir / "students.json"
cleaned.to_json(json_output, orient="records", force_ascii=False, indent=2)
print("已保存：", json_output)
print(pd.read_json(json_output, orient="records"))


print("\n格式选择：")
print("CSV    -> 通用、可直接查看，但类型信息有限")
print("JSON   -> 适合接口和嵌套结构，跨语言方便")
print("Pickle -> Python 中还原方便，但只读取可信文件")
print("Excel  -> 适合人工查看，通常需要安装 openpyxl")
