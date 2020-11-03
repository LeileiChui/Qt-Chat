"""
@File: utils.py
@time: 2020/11/4 3:14 上午
@Version: python3.8
@Author: Leilei Chui
@Contact: leilei.chui@gmail.com
@License: MIT Licence 
@Software: PyCharm
"""
import qtawesome
from PyQt5 import QtWidgets, QtCore, QtGui


def new_button(parent, size, icon_type: str, color: str = 'black'):
    icon = qtawesome.icon('fa.beer', color)
    button = QtWidgets.QPushButton(icon=icon, parent=parent)
    button.setIconSize(QtCore.QSize(size, size))
    button.setStyleSheet("background: transparent")
    button.setMaximumSize(size, size)
    button.setMinimumSize(size, size)
    button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    return button
