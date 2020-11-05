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
                uid = data_pack.login_data.uid
                password = data_pack.login_data.password
                resp_data_pack = DataPack()
                resp_data_pack.type = 'login_ack'
                resp_data_pack.id = str(uuid.uuid4())
                resp_data_pack.timeStamp = time.time()
                resp_data_pack.ack_data.ack_id = data_pack.id

                if not self.chat_server.db.login(uid, password):
                    resp_data_pack.ack_data.login_status = False
                    send_buffer.append(resp_data_pack)
                else:
                    resp_data_pack.ack_data.login_status = True
                    # session 计算规则：(uid+当前整形时间戳).md5
                    resp_data_pack.ack_data.session = utils.cal_session(data_pack.login_data.uid)
                    print(data_pack.login_data.uid, '登陆成功')
                    send_buffer.append(resp_data_pack)

                    init_data_pack = DataPack()
                    init_data_pack.type = 'init_data'
                    init_data_pack.id = str(uuid.uuid4())
                    init_data_pack.timeStamp = time.time()
                    user_info = self.chat_server.db.getUserInfo(uid)
                    init_data_pack.user_info.uid = str(user_info[0])
                    init_data_pack.user_info.nick_name = user_info[1]
                    if user_info[2] is not None:
                        init_data_pack.user_info.avatar = user_info[2]
                    else:
                        init_data_pack.user_info.avatar = b''
                    friends_info = self.chat_server.db.getFriends(uid)
                    for info in friends_info:
                        friend = UserInfo()
                        friend.uid = str(info[0])
                        friend.nick_name = info[1]
                        if info[2] is None:
                            friend.avatar = b''
                        else:
                            friend.avatar = info[2]
                        init_data_pack.friends_info.append(friend)

                    groups_info = self.chat_server.db.getGroups(uid)
                    for info in groups_info:
                        group = GroupInfo()
                        group.g_id = str(info[0])
                        group.g_name = info[1]
                        group.creat_time = info[2]
                        group.g_author_id = str(info[3])
                        group.g_nick_name = info[4]
                        init_data_pack.groups_info.append(group)
                    send_buffer.append(init_data_pack)
