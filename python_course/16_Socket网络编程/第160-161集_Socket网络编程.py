"""
第 160～161 集：Socket 服务端与客户端。

本文件会在本机 127.0.0.1 上临时启动服务端和客户端，使用系统分配的空闲端口，
不访问公网，也不会一直阻塞等待。
"""

import socket
import threading


def show_title(title):
    print(f"\n{'=' * 12} {title} {'=' * 12}")


HOST = "127.0.0.1"  # 回环地址，只允许本机通信。
BUFFER_SIZE = 1024


show_title("1. 第 160 集：Socket 服务端")

# TCP 服务端固定流程：socket -> bind -> listen -> accept -> recv/send -> close。
# bind((host, 0)) 中的 0 表示让操作系统自动选择一个当前可用端口。
server_ready = threading.Event()
server_info = {}


def run_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((HOST, 0))
        server_socket.listen(1)
        server_info["port"] = server_socket.getsockname()[1]
        print(f"服务端正在监听 {HOST}:{server_info['port']}")
        server_ready.set()

        # accept 返回“用于和该客户端通信的 socket”以及客户端地址。
        connection, client_address = server_socket.accept()
        with connection:
            print("服务端收到连接：", client_address)
            data = connection.recv(BUFFER_SIZE)
            message = data.decode("utf-8")
            print("服务端收到：", message)
            connection.sendall(f"服务端已收到：{message}".encode("utf-8"))


server_thread = threading.Thread(target=run_server, name="本地Socket服务端")
server_thread.start()
server_ready.wait(timeout=2)


show_title("2. 第 161 集：Socket 客户端")

# TCP 客户端固定流程：socket -> connect -> send/recv -> close。
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.settimeout(2)
    client_socket.connect((HOST, server_info["port"]))
    client_socket.sendall("你好，Socket！".encode("utf-8"))
    reply = client_socket.recv(BUFFER_SIZE).decode("utf-8")
    print("客户端收到：", reply)

server_thread.join(timeout=2)
if server_thread.is_alive():
    raise RuntimeError("服务端线程没有按预期结束")


show_title("3. 服务端与客户端横向比较")

comparison = [
    ("创建", "socket()", "socket()"),
    ("建立连接", "bind/listen/accept", "connect"),
    ("发送", "send/sendall", "send/sendall"),
    ("接收", "recv", "recv"),
    ("结束", "close（with 自动完成）", "close（with 自动完成）"),
]
print(f"{'步骤':<8} | {'服务端':<22} | 客户端")
for step, server_action, client_action in comparison:
    print(f"{step:<8} | {server_action:<22} | {client_action}")

# send/recv 处理的是 bytes，因此字符串发送前要 encode，收到后要 decode。
# TCP 是字节流协议，真实项目不能假设一次 recv 就得到一条完整消息，通常需要
# 设计消息长度、分隔符或其他应用层协议。本例消息很短，仅用于入门演示。
