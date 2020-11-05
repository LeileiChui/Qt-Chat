"""
@File: chat_list_item.py
@time: 2020/11/5 8:57 上午
@Version: python3.8
@Author: Leilei Chui
@Contact: leilei.chui@gmail.com
@License: MIT Licence 
@Software: PyCharm
"""
import sys

from PyQt5 import QtCore
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QVBoxLayout, QApplication, QPushButton

from IconButton import IconButton
from msg_item import Ui_Widget


class chat_list_item(QWidget):
    def __init__(self):
        super(chat_list_item, self).__init__()
        self.setFixedSize(240, 70)
        self.setStyleSheet('QWidget{background:white;}')
        self.main_layout = QHBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        self.left_widget = QWidget(self)
        self.left_widget.setFixedSize(70, 70)
        self.left_widget_layout = QHBoxLayout(self.left_widget)
        self.left_widget_layout.setContentsMargins(0, 0, 0, 0)
        self.left_widget_layout.setSpacing(0)

        self.close_btn = IconButton('times', 20, 0.8)

        self.close_btn.setParent(self.left_widget)
        self.left_widget_layout.addWidget(self.close_btn)

        self.avatar = QWidget(self.left_widget)
        self.avatar.setFixedSize(40, 40)
        self.avatar.setStyleSheet("background:rgb(82, 255, 53);border-radius:20;")
        self.left_widget_layout.addWidget(self.avatar)
        self.main_layout.addWidget(self.left_widget)

        self.right_widget = QWidget(self)
        self.preview_layout = QVBoxLayout(self.right_widget)
        self.preview_layout.setContentsMargins(0, 0, 0, 0)
        self.preview_layout.setSpacing(0)

        self.name = QLabel(self.right_widget)
        self.name.setFixedHeight(30)
        self.name.setText('兜率宫')
        font = QFont()
        font.setFamily("PingFang SC")
        font.setPointSize(15)
        self.name.setFont(font)
        self.name.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.preview_layout.addWidget(self.name, 0, QtCore.Qt.AlignBottom)
        self.spacer_0 = QLabel(self.right_widget)
        self.spacer_0.setFixedHeight(10)
        self.preview_layout.addWidget(self.spacer_0)
        self.msg_preview = QLabel(self.right_widget)
        self.msg_preview.setText('黄生鲜：测试消息')
        self.msg_preview.setFixedHeight(30)
        self.msg_preview.setStyleSheet('color:grey;')
        self.msg_preview.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.preview_layout.addWidget(self.msg_preview, 0, QtCore.Qt.AlignTop)
        self.main_layout.addWidget(self.right_widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = chat_list_item()
    w.setWindowFlag(QtCore.Qt.FramelessWindowHint)
    w.show()
    sys.exit(app.exec_())
