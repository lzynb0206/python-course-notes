"""
第 127～138 集：SQL 与 MySQL。

本文件把 SQL 语法按 DDL、DML、DQL 分类，并演示 Python 如何连接 MySQL。
默认只打印 SQL，不会连接或修改数据库；准备好本机 MySQL 后，把
RUN_MYSQL_DEMO 改为 True，并填写自己的连接信息即可。
"""

RUN_MYSQL_DEMO = False


def show_title(title):
    print(f"\n{'=' * 12} {title} {'=' * 12}")


show_title("1. 第 127～130 集：数据库与 MySQL 基础")

# 数据库用于有组织地保存大量数据；MySQL 是一种关系型数据库管理系统。
# 常见层级：MySQL 服务 -> 数据库（database）-> 表（table）-> 行和列。
#
# MySQL 客户端常用命令：
# mysql -u root -p          登录本机 MySQL
# SHOW DATABASES;           查看数据库
# USE 数据库名;             切换数据库
# SHOW TABLES;              查看当前数据库中的表
# EXIT;                     退出客户端

MYSQL_BASIC_SQL = """
SHOW DATABASES;
CREATE DATABASE IF NOT EXISTS python_study
    DEFAULT CHARACTER SET utf8mb4;
USE python_study;
SHOW TABLES;
""".strip()
print(MYSQL_BASIC_SQL)


show_title("2. 第 131 集：SQL 基础与 DDL")

# SQL 关键字不区分大小写，通常把关键字大写以提高可读性。
# DDL（Data Definition Language）负责定义数据库和表的结构。
DDL_SQL = """
CREATE TABLE IF NOT EXISTS students (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(20) NOT NULL,
    age INT,
    city VARCHAR(20),
    score DECIMAL(5, 2)
);

ALTER TABLE students ADD COLUMN created_at DATETIME;
DESC students;

-- 删除操作不可逆，学习时一定先确认对象名称：
-- DROP TABLE students;
-- DROP DATABASE python_study;
""".strip()
print(DDL_SQL)


show_title("3. 第 132 集：DML 数据操作")

# DML（Data Manipulation Language）负责新增、修改和删除表中的数据。
DML_SQL = """
INSERT INTO students (name, age, city, score)
VALUES ('小明', 18, '北京', 88.5),
       ('小红', 19, '上海', 95.0),
       ('小刚', 20, '北京', 76.0);

UPDATE students
SET score = 90
WHERE name = '小明';

DELETE FROM students
WHERE name = '小刚';
""".strip()
print(DML_SQL)

# UPDATE 或 DELETE 如果漏写 WHERE，可能影响整张表，这是最需要警惕的错误。


show_title("4. 第 133 集：DQL 基础查询")

# DQL（Data Query Language）使用 SELECT 查询数据，不直接修改原数据。
DQL_BASIC_SQL = """
SELECT * FROM students;
SELECT name, score FROM students;
SELECT DISTINCT city FROM students;
SELECT name AS 姓名, score AS 成绩 FROM students;

SELECT * FROM students WHERE age >= 18;
SELECT * FROM students WHERE city = '北京' AND score >= 80;
SELECT * FROM students WHERE city = '北京' OR city = '上海';
SELECT * FROM students WHERE score BETWEEN 80 AND 100;
SELECT * FROM students WHERE name LIKE '小%';
SELECT * FROM students WHERE city IN ('北京', '上海');
SELECT * FROM students WHERE created_at IS NULL;
""".strip()
print(DQL_BASIC_SQL)


show_title("5. 第 134 集：分组聚合")

# 聚合函数把多行数据汇总成一个结果：COUNT、MAX、MIN、AVG、SUM。
# WHERE 在分组前过滤原始行；HAVING 在分组后过滤聚合结果。
DQL_GROUP_SQL = """
SELECT COUNT(*) AS student_count FROM students;
SELECT MAX(score), MIN(score), AVG(score), SUM(score) FROM students;

SELECT city,
       COUNT(*) AS student_count,
       ROUND(AVG(score), 2) AS average_score
FROM students
WHERE score IS NOT NULL
GROUP BY city
HAVING AVG(score) >= 80;
""".strip()
print(DQL_GROUP_SQL)


show_title("6. 第 135 集：排序与分页")

# ASC 是升序（默认），DESC 是降序。
# LIMIT 起始下标, 数量；起始下标从 0 开始。
DQL_PAGE_SQL = """
SELECT name, city, score
FROM students
ORDER BY score DESC, age ASC;

-- 每页 10 条：第 1 页 LIMIT 0, 10；第 2 页 LIMIT 10, 10。
SELECT * FROM students ORDER BY id LIMIT 0, 10;
SELECT * FROM students ORDER BY id LIMIT 10, 10;
""".strip()
print(DQL_PAGE_SQL)


show_title("7. SQL 分类横向比较")

sql_comparison = [
    ("DDL", "定义结构", "CREATE / ALTER / DROP / SHOW / USE"),
    ("DML", "修改数据", "INSERT / UPDATE / DELETE"),
    ("DQL", "查询数据", "SELECT / WHERE / GROUP BY / ORDER BY / LIMIT"),
]
for category, purpose, keywords in sql_comparison:
    print(f"{category:<3} | {purpose:<4} | {keywords}")


show_title("8. 第 136～137 集：Python 操作 MySQL")


def run_mysql_demo():
    """连接本机 MySQL，完成查询与参数化插入。

    运行前先执行：python3 -m pip install pymysql
    请把 password 改成自己的密码。示例使用参数化 SQL，避免手动拼接值。
    """
    try:
        from pymysql import Connection
    except ImportError:
        print("尚未安装 PyMySQL：python3 -m pip install pymysql")
        return

    connection = None
    try:
        connection = Connection(
            host="localhost",
            port=3306,
            user="root",
            password="请填写自己的密码",
            database="python_study",
            charset="utf8mb4",
        )
        print("MySQL 版本：", connection.get_server_info())

        with connection.cursor() as cursor:
            cursor.execute("SELECT id, name, score FROM students ORDER BY id")
            for row in cursor.fetchall():
                print(row)

            # %s 是 PyMySQL 的值占位符。值与 SQL 分开传入，不要用 f-string 拼接。
            cursor.execute(
                "INSERT INTO students (name, age, city, score) VALUES (%s, %s, %s, %s)",
                ("小兰", 18, "广州", 91.5),
            )
        connection.commit()  # 提交事务后，插入结果才真正保存。
        print("插入完成，新增行 id：", cursor.lastrowid)
    except Exception as error:
        if connection is not None:
            connection.rollback()  # 失败时撤销本次尚未提交的修改。
        print("数据库操作失败：", error)
    finally:
        if connection is not None:
            connection.close()


if RUN_MYSQL_DEMO:
    run_mysql_demo()
else:
    print("数据库演示默认关闭；准备好 MySQL 后可把 RUN_MYSQL_DEMO 改为 True。")


show_title("9. 第 138 集：综合案例思路")

# 综合案例的关键步骤：读取数据 -> 清洗/转换 -> 连接数据库 -> 批量写入 -> 提交。
sales_records = [
    ("2026-01-01", "北京", "键盘", 299.0),
    ("2026-01-01", "上海", "鼠标", 129.0),
    ("2026-01-02", "北京", "显示器", 1599.0),
]
INSERT_SALE_SQL = """
INSERT INTO sales (sale_date, city, product, amount)
VALUES (%s, %s, %s, %s)
""".strip()
print("批量写入 SQL：", INSERT_SALE_SQL)
print("待写入数据：", sales_records)

# 真正批量写入时可使用：
# cursor.executemany(INSERT_SALE_SQL, sales_records)
# connection.commit()
# 如果输入来自文件，应先校验日期、金额和字段数量，再写入数据库。
