"""文件工具模块：对应第 98 集综合案例。"""

__all__ = ["print_file_info", "append_to_file"]


def print_file_info(file_name):
    """读取并打印文件；发生异常时给出提示；最终确保文件关闭。"""
    file = None
    try:
        file = open(file_name, "r", encoding="utf-8")
        content = file.read()
        print("文件内容如下：")
        print(content)
    except Exception as error:
        print(f"文件读取失败：{error}")
    finally:
        if file:
            file.close()
            print("文件已关闭")


def append_to_file(file_name, data):
    """把 data 追加到文件末尾。"""
    file = None
    try:
        file = open(file_name, "a", encoding="utf-8")
        file.write(data)
    except Exception as error:
        print(f"文件追加失败：{error}")
    finally:
        if file:
            file.close()

