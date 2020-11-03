"""
@File: IconButton.py
@time: 2020/11/4 4:56 上午
@Version: python3.8
@Author: Leilei Chui
@Contact: leilei.chui@gmail.com
@License: MIT Licence 
@Software: PyCharm
"""
from PyQt5 import QtCore
from PyQt5.QtCore import QEvent, QSize
from PyQt5.QtGui import QIcon, QCursor
from PyQt5.QtWidgets import QPushButton


class IconButton(QPushButton):
    icon_path = {
        'close': 'res/close.png',
        'close_hover': 'res/close_hover.png',
        'login': 'res/login.png',
        'login_hover': 'res/login_hover.png'
    }

    def __init__(self, icon_name, size, factor: float = 1):
        super(IconButton, self).__init__()
        self.icon = QIcon(self.icon_path[icon_name])
        self.hover_icon = QIcon(self.icon_path[icon_name + '_hover'])
        self.setIcon(self.icon)
        self.setIconSize(QSize(int(size * factor), int(size * factor)))
        self.setMaximumSize(size, size)
        self.setMinimumSize(size, size)
        self.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

    def enterEvent(self, event: QEvent) -> None:
        self.setIcon(self.hover_icon)

    def leaveEvent(self, event: QEvent) -> None:
        self.setIcon(self.icon)
