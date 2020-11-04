"""
@File: main.py
@time: 2020/11/3 6:11 上午
@Version: python3.8
@Author: Leilei Chui
@Contact: leilei.chui@gmail.com
@License: MIT Licence 
@Software: PyCharm
"""
import socket
import struct
import sys
import time

from PyQt5.QtWidgets import QApplication

from ChatApp import ChatApp
from protobuf.DataPack_pb2 import *


def client(addr):
    while True:
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((addr, 1234))
            print("连接成功")
            break
        except ConnectionRefusedError:
            print("服务器未启动，等待重连")
            time.sleep(1)
        except TimeoutError:
            print("服务器未启动，等待连接")
            time.sleep(10)
    while True:
        input_data = input("输入包类型，id：")
        input_list = input_data.split()
        if input_data == "quit":
            client.close()
            break
        account = DataPack()
        account.type = input_list[0]
        account.id = input_list[1]
        byte_data = account.SerializeToString()
        byte_length = struct.pack('>L', len(byte_data))
        client.send(byte_length)
        client.send(byte_data)
        byte_length = client.recv(4)
        length = struct.unpack('>L', byte_length)[0]
        byte_data = client.recv(length)
        data_pack = DataPack()
        data_pack.ParseFromString(byte_data)
        print(data_pack.type, data_pack.id)
        if not byte_data:
            client.close()
            print('与服务器断开连接')
            break


if __name__ == '__main__':
    app=QApplication(sys.argv)
    chat_app=ChatApp()
    chat_app.run()
    sys.exit(app.exec_())
