import socket
import struct
import time
from protobuf.DataPack_pb2 import *
import conf
from PyQt5.QtCore import QObject, pyqtSignal


class Client(QObject):
    login_result = pyqtSignal(DataPack)
    connect_info = pyqtSignal(bool)

    def __init__(self):
        super(Client, self).__init__()
        self.send_buffer = []
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.quit = False

    def run(self):
        while not self.quit:
            try:
                self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.client.connect(conf.server_addr)
                print("连接成功")
                self.connect_info.emit(True)
                break
            except ConnectionRefusedError:
                print("服务器未启动，等待重连")
                self.connect_info.emit(False)
                time.sleep(1)
            except TimeoutError:
                print("服务器未启动，等待连接")
                self.connect_info.emit(False)
                time.sleep(1)
            # except OSError:
            #     break
        self.client.setblocking(False)
        while not self.quit:
            self.sender()
            data = self.receive()
            if data is None:
                continue
            data_pack = DataPack()
            data_pack.ParseFromString(data)
            if data_pack.type == "login_ack":
                self.login_result.emit(data_pack)

    def sender(self):
        for data_pack in self.send_buffer:
            byte_data = data_pack.SerializeToString()
            byte_length = struct.pack('>L', len(byte_data))
            self.client.send(byte_length)
            self.client.send(byte_data)
            print("发送消息")
        self.send_buffer.clear()

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
            pass
