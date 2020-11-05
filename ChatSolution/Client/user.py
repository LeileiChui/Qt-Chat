"""
@File: user.py
@time: 2020/11/5 10:31 上午
@Version: python3.8
@Author: Leilei Chui
@Contact: leilei.chui@gmail.com
@License: MIT Licence 
@Software: PyCharm
"""
from PyQt5.QtCore import QObject, pyqtSignal


class User(QObject):
    update_chat_with = pyqtSignal()

    def __init__(self):
        super(User, self).__init__()
        self.uid = ''
        self.nick_name = ''
        self.avatar = ''
        self.isMale = None
        self.registration_time = 0
        self.session = ''
        self.friends = {}
        self.groups = {}
        self.friends_msg_history = {}

    def init_data(self, p_data_pack):
        self.uid = p_data_pack.user_info.uid
        self.nick_name = p_data_pack.user_info.nick_name
        self.avatar = p_data_pack.user_info.avatar
        self.isMale = p_data_pack.user_info.isMale
        self.registration_time = p_data_pack.user_info.registration_time
        for friend in p_data_pack.friends_info:
            self.friends[friend.uid] = friend
        for group in p_data_pack.groups_info:
            self.groups[group.g_id] = group

        self.update_chat_with.emit()
