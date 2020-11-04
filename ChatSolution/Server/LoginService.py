"""
@File: LoginService.py
@time: 2020/11/4 8:27 下午
@Version: python3.8
@Author: Leilei Chui
@Contact: leilei.chui@gmail.com
@License: MIT Licence 
@Software: PyCharm
"""
import time
import uuid

import utils
from protobuf.DataPack_pb2 import *


class LoginService:
    def __init__(self, chat_server):
        self.data_buffer = []
        self.chat_server = chat_server
        self.quit = False

    def run(self):
        while not self.chat_server.quit:
            if len(self.data_buffer) != 0:
                send_buffer, data_pack = self.data_buffer.pop(0)
                resp_data_pack = DataPack()
                resp_data_pack.type = 'login_ack'
                resp_data_pack.id = str(uuid.uuid4())
                resp_data_pack.timeStamp = time.time()
                resp_data_pack.ack_data.ack_id = data_pack.id

                if self.chat_server.db.login(data_pack.login_data.uid, data_pack.login_data.password):
                    resp_data_pack.ack_data.login_status = True
                    # session 计算规则：(uid+当前整形时间戳).md5
                    resp_data_pack.ack_data.session = utils.cal_session(data_pack.login_data.uid)
                    print(data_pack.login_data.uid, '登陆成功')
                else:
                    resp_data_pack.ack_data.login_status = False
                send_buffer.append(resp_data_pack)
