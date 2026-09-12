"""
第 85～90 集：Python 文件操作。

本文件会在当前目录的 runtime_data/ 中创建练习文件，不会修改你的其他文件。
重复运行时会重新生成练习数据，因此每次输出一致。
"""

from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
RUNTIME_DIR = BASE_DIR / "runtime_data"
RUNTIME_DIR.mkdir(exist_ok=True)


def show_title(title):
    print(f"\n{'=' * 12} {title} {'=' * 12}")


show_title("1. 第 85 集：文件编码")

# 编码规定“文字怎样转换成计算机保存的二进制数据”。
# UTF-8 是最常用的编码之一；中文通常需要 3 个字节，英文通常需要 1 个字节。
text = "你好，Python"
utf8_data = text.encode("utf-8")
print("原字符串：", text)
print("编码后的字节：", utf8_data)
print("解码回来：", utf8_data.decode("utf-8"))

# 打开文本文件时，读取使用的编码应当和文件保存时的编码一致。
# 编码不一致，可能出现 UnicodeDecodeError 或乱码。


show_title("2. 第 86 集：准备一个读取练习文件")

read_file_path = RUNTIME_DIR / "read_demo.txt"
read_file_path.write_text(
    "itheima is a brand of itcast\n"
    "Python is easy to learn\n"
    "itheima teaches Python\n",
    encoding="utf-8",
)

# 课程中的基础写法：open -> read -> close。
file = open(read_file_path, "r", encoding="utf-8")
content = file.read()
file.close()
print("read() 读取全部内容：")
print(content)


show_title("3. read()、readline()、readlines() 横向比较")

with open(read_file_path, "r", encoding="utf-8") as file:
    first_five = file.read(5)
    print("read(5)：", first_five)

with open(read_file_path, "r", encoding="utf-8") as file:
    first_line = file.readline()
    print("readline()：", repr(first_line))

with open(read_file_path, "r", encoding="utf-8") as file:
    all_lines = file.readlines()
    print("readlines()：", all_lines)

# read(n)       -> 读取指定数量字符；不传 n 就读取全部，返回 str。
# readline()    -> 读取一行，通常包含行尾的 \n，返回 str。
# readlines()   -> 一次读取所有行，返回 list[str]。
# for line in f -> 逐行读取，适合较大的文件。


show_title("4. 文件指针与 with open")

with open(read_file_path, "r", encoding="utf-8") as file:
    print("第一次 read(7)：", file.read(7))
    print("第二次 read(7)：", file.read(7))

# 同一个文件对象连续读取时，第二次会从上一次结束的位置继续。
# with 代码块结束后会自动关闭文件，是实际开发中的推荐写法。


show_title("5. 第 87 集练习：统计 itheima 出现次数")

word_count = 0
with open(read_file_path, "r", encoding="utf-8") as file:
    for line in file:
        # strip() 去掉行首和行尾的空白字符，包括 \n。
        clean_line = line.strip()
        word_count += clean_line.count("itheima")

print("itheima 出现次数：", word_count)     # 2


show_title("6. strip、split、replace 横向比较")

line = "  apple,banana,orange\n"
print("原字符串：", repr(line))
print("strip 后：", repr(line.strip()))
print("split 后：", line.strip().split(","))
print("replace 后：", line.strip().replace(",", "|"))

# strip()            -> 去掉字符串两端的字符，不改中间内容。
# split(",")         -> 按逗号切开，返回列表。
# replace(",", "|") -> 把字符串中的逗号替换成竖线，返回新字符串。
# 字符串不可修改，所以这些方法都不会修改原字符串，而是返回新字符串。


show_title("7. 第 88 集：写入模式 w")

write_file_path = RUNTIME_DIR / "write_demo.txt"

# w 模式：文件不存在就创建；文件存在就清空原内容后重新写入。
with open(write_file_path, "w", encoding="utf-8") as file:
    file.write("第一行：使用 w 模式写入\n")
    file.write("第二行：write 不会自动换行\n")
    # flush() 可以把缓冲区中的数据立即写入文件，close() 前也会自动刷新。
    file.flush()

print(write_file_path.read_text(encoding="utf-8"))


show_title("8. 第 89 集：追加模式 a")

# a 模式：保留原内容，把新内容添加到文件末尾；文件不存在也会创建。
with open(write_file_path, "a", encoding="utf-8") as file:
    file.write("第三行：使用 a 模式追加\n")

print(write_file_path.read_text(encoding="utf-8"))


show_title("9. 第 90 集：账单文件备份综合案例")

source_path = RUNTIME_DIR / "bill.txt"
backup_path = RUNTIME_DIR / "bill_backup.txt"

source_path.write_text(
    "name,date,money,type,remarks\n"
    "周杰伦,2022-01-01,100000,消费,正式\n"
    "周杰伦,2022-01-02,300000,收入,正式\n"
    "林俊杰,2022-01-03,100000,消费,测试\n"
    "林俊杰,2022-01-04,300000,收入,正式\n"
    "张学友,2022-01-05,100000,消费,测试\n",
    encoding="utf-8",
)

saved_count = 0
skipped_count = 0

# 第一个 for 逐行读取源文件；这里没有第二个嵌套 for。
with open(source_path, "r", encoding="utf-8") as source_file:
    with open(backup_path, "w", encoding="utf-8") as target_file:
        for line in source_file:
            # 先去掉末尾换行，再按逗号切分，[-1] 取得最后一列 remarks。
            line_type = line.strip().split(",")[-1]

            if line_type == "测试":
                skipped_count += 1
                continue                  # 跳过本轮，不执行下面的 write

            # 写入原始 line，才能保留它原来的换行符。
            target_file.write(line)
            saved_count += 1

print(f"备份完成：写入 {saved_count} 行，跳过 {skipped_count} 行")
print("备份文件内容：")
print(backup_path.read_text(encoding="utf-8"))

print("练习文件目录：", RUNTIME_DIR)

