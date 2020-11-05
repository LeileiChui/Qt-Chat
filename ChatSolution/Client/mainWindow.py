"""
@File: mainWindow.py
@time: 2020/11/5 2:22 上午
@Version: python3.8
@Author: Leilei Chui
@Contact: leilei.chui@gmail.com
@License: MIT Licence 
@Software: PyCharm
"""
import sys

import typing
from PyQt5 import QtCore, sip
from PyQt5.QtGui import QMouseEvent, QFont
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QHBoxLayout, QLineEdit, QWidgetAction, QLabel, \
    QListWidget, QPlainTextEdit

from IconButton import IconButton
from UI import Ui_Widget


class MainWindow(QWidget):
    def __init__(self, app):
        super(MainWindow, self).__init__()
        # self.ui = Ui_Widget()
        # self.ui.setupUi(self)
        self.app = app
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.resize(1000, 618)
        self.setMinimumSize(1000, 618)
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.window_title = QWidget(self)
        # self.window_title.setStyleSheet('background-color:#e1e1e2;')
        self.window_title.setFixedHeight(50)
        self.window_title_layout = QHBoxLayout(self.window_title)
        self.window_title_layout.setContentsMargins(0, 0, 0, 0)
        self.window_title_layout.setSpacing(0)

        self.title_left = QWidget(self.window_title)
        self.title_left.setFixedSize(240, 46)

        self.title_left_layout = QHBoxLayout(self.title_left)
        self.title_left_layout.setContentsMargins(0, 0, 0, 0)
        self.title_left_layout.setSpacing(15)

        self.exit_btn = IconButton('close', 30, 0.6)
        self.exit_btn.setParent(self.title_left)
        self.title_left_layout.addWidget(self.exit_btn)
        font = QFont()
        font.setFamily("PingFang SC")
        font.setPointSize(15)
        self.search_input = QLineEdit(self.title_left)
        self.setFont(font)
        self.search_input.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.search_input.setAttribute(QtCore.Qt.WA_MacShowFocusRect, 0)
        self.search_input.setAlignment(QtCore.Qt.AlignCenter)
        self.search_input.setFixedSize(160, 30)
        self.search_input_icon = IconButton('search', 30, 0.7)
        search_action = QWidgetAction(self.search_input)
        search_action.setDefaultWidget(self.search_input_icon)
        self.search_input.addAction(search_action)
        self.search_input.setStyleSheet('border-radius:15;')
        self.title_left_layout.addWidget(self.search_input)

        self.add_friend_btn = IconButton('add', 30, 0.7)
        self.add_friend_btn.setParent(self.title_left)
        self.title_left_layout.addWidget(self.add_friend_btn)

        self.window_title_layout.addWidget(self.title_left)

        self.window_title_layout.addStretch(1)

        self.goto_chat_btn = IconButton('chat', 50, 0.5)
        self.goto_chat_btn.setParent(self.window_title)
        self.goto_chat_btn.setFixedSize(50, 50)
        self.window_title_layout.addWidget(self.goto_chat_btn)

        self.spacer_2 = QLabel(self.window_title)
        self.spacer_2.setFixedWidth(20)

        self.window_title_layout.addWidget(self.spacer_2)

        self.goto_manager_btn = IconButton('person', 50, 0.5)
        self.goto_manager_btn.setFixedSize(50, 50)
        self.goto_manager_btn.setParent(self.window_title)
        self.window_title_layout.addWidget(self.goto_manager_btn)

        self.window_title_layout.addStretch(2)

        self.layout.addWidget(self.window_title)

        self.mainArea = QWidget(self)
        self.mainArea_layout = QHBoxLayout(self.mainArea)
        self.mainArea_layout.setContentsMargins(0, 0, 0, 0)
        self.mainArea_layout.setSpacing(0)
        self.chat_list = QListWidget(self.mainArea)
        self.chat_list.setStyleSheet('border-left:none;border-top:none;border-bottom:none;')
        self.chat_list.setFixedWidth(240)
        self.mainArea_layout.addWidget(self.chat_list)

        self.right_bottom_widget = QWidget(self.mainArea)
        self.right_bottom_widget_layout = QVBoxLayout(self.right_bottom_widget)
        self.right_bottom_widget_layout.setContentsMargins(0, 0, 0, 0)
        self.right_bottom_widget_layout.setSpacing(0)
        self.chat_record = QListWidget(self.right_bottom_widget)
        self.chat_record.setStyleSheet('border-left:none;border-top:none;border-right:none;')
        self.right_bottom_widget_layout.addWidget(self.chat_record)
        self.quick_op_btns = QWidget(self.right_bottom_widget)
        self.quick_op_btns.setStyleSheet('background:white;')
        self.quick_op_btns.setFixedHeight(35)
        self.quick_op_btns_layout = QHBoxLayout(self.quick_op_btns)
        self.quick_op_btns_layout.setContentsMargins(0, 0, 0, 0)
        self.quick_op_btns_layout.setSpacing(12)

        self.chose_emoji_btn = IconButton('emoji', 35, 0.7)
        self.chose_emoji_btn.setFixedSize(35, 35)
        self.chose_emoji_btn.setParent(self.quick_op_btns)
        self.quick_op_btns_layout.addWidget(self.chose_emoji_btn)

        self.screenshut_btn = IconButton('screen_shut', 35, 0.7)
        self.screenshut_btn.setFixedSize(35, 35)
        self.screenshut_btn.setParent(self.quick_op_btns)
        self.quick_op_btns_layout.addWidget(self.screenshut_btn)

        self.send_file_btn = IconButton('file', 35, 0.7)
        self.send_file_btn.setFixedSize(35, 35)
        self.send_file_btn.setParent(self.quick_op_btns)
        self.quick_op_btns_layout.addWidget(self.send_file_btn)

        self.quick_op_btns_layout.addStretch(1)

        self.right_bottom_widget_layout.addWidget(self.quick_op_btns)

        self.msg_edit = QPlainTextEdit(self.right_bottom_widget)
        self.msg_edit.setStyleSheet('border-top:none;')
        self.msg_edit.setFixedHeight(120)

        self.msg_edit.setFont(font)
        self.right_bottom_widget_layout.addWidget(self.msg_edit)
        self.mainArea_layout.addWidget(self.right_bottom_widget)
        self.layout.addWidget(self.mainArea)
        self.setMouseTracking(True)
        self.initDrag()

        self.exit_btn.clicked.connect(self.app.quit)
        self.goto_chat_btn.clicked.connect(self.switch_page)
        self.goto_manager_btn.clicked.connect(self.switch_page)

    def switch_page(self):
        if self.sender() == self.goto_chat_btn:
            self.goto_chat_btn.active_flag = True
            self.goto_manager_btn.active_flag = False
            self.goto_manager_btn.setIcon(self.goto_manager_btn.icon)

        elif self.sender() == self.goto_manager_btn:
            self.goto_chat_btn.active_flag = False
            self.goto_chat_btn.setIcon(self.goto_chat_btn.icon)
            self.goto_manager_btn.active_flag = True

    def initDrag(self):
        self._padding = 5
        # 设置鼠标跟踪判断扳机默认值
        self._move_drag = False
        self._corner_drag = False
        self._bottom_drag = False
        self._right_drag = False
        self._right_rect = [QtCore.QPoint(x, y) for x in range(self.width() - self._padding, self.width() + 1)
                            for y in range(1, self.height() - self._padding)]
        self._bottom_rect = [QtCore.QPoint(x, y) for x in range(1, self.width() - self._padding)
                             for y in range(self.height() - self._padding, self.height() + 1)]
        self._corner_rect = [QtCore.QPoint(x, y) for x in range(self.width() - self._padding, self.width() + 1)
                             for y in range(self.height() - self._padding, self.height() + 1)]

    def mousePressEvent(self, event):
        # 重写鼠标点击的事件
        if (event.button() == QtCore.Qt.LeftButton) and (event.pos() in self._corner_rect):
            # 鼠标左键点击右下角边界区域
            self._corner_drag = True
            event.accept()
        elif (event.button() == QtCore.Qt.LeftButton) and (event.pos() in self._right_rect):
            # 鼠标左键点击右侧边界区域
            self._right_drag = True
            event.accept()
        elif (event.button() == QtCore.Qt.LeftButton) and (event.pos() in self._bottom_rect):
            # 鼠标左键点击下侧边界区域
            self._bottom_drag = True
            event.accept()
        elif (event.button() == QtCore.Qt.LeftButton) and (event.y() < self.window_title.height()):
            # 鼠标左键点击标题栏区域
            self._move_drag = True
            self.move_DragPosition = event.globalPos() - self.pos()
            event.accept()

    def mouseMoveEvent(self, QMouseEvent):
        # 判断鼠标位置切换鼠标手势
        if QMouseEvent.pos() in self._corner_rect:
            self.setCursor(QtCore.Qt.SizeFDiagCursor)
        elif QMouseEvent.pos() in self._bottom_rect:
            self.setCursor(QtCore.Qt.SizeVerCursor)
        elif QMouseEvent.pos() in self._right_rect:
            self.setCursor(QtCore.Qt.SizeHorCursor)
        else:
            self.setCursor(QtCore.Qt.ArrowCursor)
        # 当鼠标左键点击不放及满足点击区域的要求后，分别实现不同的窗口调整
        # 没有定义左方和上方相关的5个方向，主要是因为实现起来不难，但是效果很差，拖放的时候窗口闪烁，再研究研究是否有更好的实现
        if QtCore.Qt.LeftButton and self._right_drag:
            # 右侧调整窗口宽度
            self.resize(QMouseEvent.pos().x(), self.height())
            QMouseEvent.accept()
        elif QtCore.Qt.LeftButton and self._bottom_drag:
            # 下侧调整窗口高度
            self.resize(self.width(), QMouseEvent.pos().y())
            QMouseEvent.accept()
        elif QtCore.Qt.LeftButton and self._corner_drag:
            # 右下角同时调整高度和宽度
            self.resize(QMouseEvent.pos().x(), QMouseEvent.pos().y())
            QMouseEvent.accept()
        elif QtCore.Qt.LeftButton and self._move_drag:
            # 标题栏拖放窗口位置
            self.move(QMouseEvent.globalPos() - self.move_DragPosition)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        # 鼠标释放后，各扳机复位
        self._move_drag = False
        self._corner_drag = False
        self._bottom_drag = False
        self._right_drag = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.setWindowFlag(QtCore.Qt.FramelessWindowHint)
    w.show()
    sys.exit(app.exec_())
