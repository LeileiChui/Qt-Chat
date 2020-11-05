"""
@File: chat_list_item.py
@time: 2020/11/5 8:57 上午
@Version: python3.8
@Author: Leilei Chui
@Contact: leilei.chui@gmail.com
@License: MIT Licence 
@Software: PyCharm
"""
from PyQt5.QtWidgets import QWidget, QHBoxLayout

from IconButton import IconButton


class chat_list_item(QWidget):
    def __init__(self):
        super(chat_list_item, self).__init__()
        self.setFixedSize(240, 70)
        self.setStyleSheet('background:white;')
        self.main_layout = QHBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)
        self.close_btn = IconButton('times', 20, 0.7)
        self.close_btn.setParent(self)
        self.close_btn.setFixedSize(20, 240)
        self.main_layout.addWidget(self.close_btn)
        self.avatar = QWidget()
