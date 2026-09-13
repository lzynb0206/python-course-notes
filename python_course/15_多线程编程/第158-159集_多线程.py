"""
第 158～159 集：多线程的概念与编程。

线程适合同时等待多个 I/O 操作，例如文件、网络请求和数据库访问。
本文件只使用标准库，可直接运行。
"""

import threading
import time


def show_title(title):
    print(f"\n{'=' * 12} {title} {'=' * 12}")


show_title("1. 第 158 集：进程与线程")

print("当前线程：", threading.current_thread().name)

# 进程：运行中的程序，资源相对独立，创建成本较高。
# 线程：进程中的执行单元，同一进程的线程共享内存，创建成本较低。
#
# CPython 的全局解释器锁（GIL）让纯 Python CPU 密集任务通常不能仅靠线程
# 获得真正的多核并行；但线程仍很适合 I/O 密集任务，因为等待 I/O 时可切换线程。


show_title("2. 第 159 集：创建和启动线程")


def download(file_name, delay=0.05):
    """用短暂停顿模拟网络下载。"""
    print(f"[{threading.current_thread().name}] 开始下载 {file_name}")
    time.sleep(delay)
    print(f"[{threading.current_thread().name}] 完成下载 {file_name}")


# target 接收函数本身，args 是位置参数元组，kwargs 是关键字参数字典。
thread_a = threading.Thread(
    target=download,
    args=("课程视频.mp4",),
    kwargs={"delay": 0.05},
    name="下载线程-A",
)
thread_b = threading.Thread(
    target=download,
    args=("课程资料.zip",),
    name="下载线程-B",
)

thread_a.start()  # start 才会创建新线程；不要直接调用 run()。
thread_b.start()

thread_a.join()   # 主线程等待子线程结束。
thread_b.join()
print("两个下载任务都结束了")


show_title("3. 共享数据与 Lock")

counter = 0
counter_lock = threading.Lock()


def safe_increment(times):
    global counter
    for _ in range(times):
        # 多个线程修改共享数据时，用锁保护“读取—计算—写回”这一整段操作。
        with counter_lock:
            counter += 1


workers = [
    threading.Thread(target=safe_increment, args=(1000,), name=f"计数线程-{index}")
    for index in range(4)
]
for worker in workers:
    worker.start()
for worker in workers:
    worker.join()
print("加锁后的计数结果：", counter)        # 4000

# Lock 能防止竞态条件，但锁得太多会降低并发性能，也可能产生死锁。
# 经验：尽量减少共享可变数据，让锁保护的代码块保持短小。


show_title("4. 常用方法横向比较")

methods = [
    ("Thread(...) ", "创建线程对象，此时任务还没开始"),
    ("start()", "启动新线程，并在新线程中执行 target"),
    ("join()", "让当前线程等待目标线程结束"),
    ("Lock", "保护共享数据，避免多个线程同时修改"),
]
for name, purpose in methods:
    print(f"{name:<12} | {purpose}")
