import socket
import struct
import threading

from MessageQueue import MessageQueue
from protobuf.DataPack_pb2 import *


class Handler:
    def __init__(self, handler_pool: dict, client: socket.socket, addr):
        self.handler_pool = handler_pool
        self.send_pool = []
        self.client = client
        self.pub_addr = addr
        self.priv_addr = None
        self.quit = False

    def sender(self):
        for data_pack in self.send_pool:
            byte_data = data_pack.SerializeToString()
            byte_length = struct.pack('>L', len(byte_data))
            self.client.send(byte_length)
            self.client.send(byte_data)
            print("发送消息")
        self.send_pool.clear()

    def receive(self):
        try:
            bytes_data_length = self.client.recv(4)
            if not bytes_data_length:
                raise RuntimeError("socket connection broken")

            length = struct.unpack('>L', bytes_data_length)[0]
            print("包长度：", length)
            chunks = []
            bytes_recd = 0
            while bytes_recd < length:
                try:
                    chunk = self.client.recv(length - bytes_recd, 2048)
                except BlockingIOError:
                    continue
                if not chunk:
                    raise RuntimeError("socket connection broken")
                chunks.append(chunk)
                bytes_recd += len(chunk)
            data = b''.join(chunks)
            print('data长度', len(data))
            return data
        except BlockingIOError:
            pass
        except RuntimeError:
            self.quit = True

    def handle_requests(self, MQ: MessageQueue):
        while not self.quit:
            # 发送
            self.sender()
            # 收消息
            bytes_data = self.receive()
            if bytes_data is None:
                continue
            print('data:', bytes_data)
            # 解析
            data_pack = DataPack()
            data_pack.ParseFromString(bytes_data)
            # 进消息队列
            MQ.recv_buffer.put((self.send_pool, data_pack))

        # 结束消息收发
        print("断开连接")
        self.client.shutdown(socket.SHUT_WR)
        self.client.close()
        self.handler_pool.pop(self.pub_addr)
        print(self.handler_pool.keys())


class Server:
    def __init__(self, ip='127.0.0.1', port=1234):
        self.handler_pool = {}
        # 启动Socket服务
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.socket.bind((ip, port))
        except OSError:
            exit(0)
        self.socket.listen(1000)
        print("服务器启动")
        # 启动消息队列
        self.MQ = MessageQueue()
        threading.Thread(target=self.MQ.run).start()

    def run(self):
        # 监听连接
        while True:
            client, addr = self.socket.accept()
            print(*addr, "连接成功")
            client.setblocking(False)
            handler = Handler(self.handler_pool, client, addr)
            threading.Thread(target=handler.handle_requests, args=(self.MQ,)).start()
            self.handler_pool[addr] = handler
            print(self.handler_pool.keys())


if __name__ == '__main__':
    server = Server()
    server.run()
