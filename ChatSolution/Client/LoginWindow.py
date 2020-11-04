"""
@File: LoginWindow.py
@time: 2020/11/4 2:51 上午
@Version: python3.8
@Author: Leilei Chui
@Contact: leilei.chui@gmail.com
@License: MIT Licence 
@Software: PyCharm
"""
import sys

from PyQt5 import Qt, QtCore, QtWidgets
from PyQt5.QtCore import QEvent, pyqtSignal
from PyQt5.QtGui import QFont, QCursor, QMouseEvent
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QApplication, QPushButton, QWidgetAction, QLineEdit, QLabel
from IconButton import IconButton


class LoginWindow(QWidget):
    quit_signal=pyqtSignal()
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.setWindowFlag(Qt.Qt.FramelessWindowHint)
        self.setMaximumSize(248, 316)
        self.setMinimumSize(248, 316)
        self.setStyleSheet("border-radius:50px;background:white;")
        self.mainLayout = QVBoxLayout(self)
        self.mainLayout.setContentsMargins(0, 0, 0, 5)
        self.mainLayout.setSpacing(0)
        self.btn_exit = IconButton('close', 30, 0.5)
        self.mainLayout.addWidget(self.btn_exit)

        self.spacer_0 = QtWidgets.QLabel(self)
        self.spacer_0.setMinimumSize(QtCore.QSize(0, 10))
        self.spacer_0.setMaximumSize(QtCore.QSize(16777215, 10))
        self.mainLayout.addWidget(self.spacer_0)

        self.label_avatar = QtWidgets.QLabel(self)
        self.label_avatar.setMinimumSize(QtCore.QSize(100, 100))
        self.label_avatar.setMaximumSize(QtCore.QSize(100, 100))
        self.label_avatar.setStyleSheet("background:rgba(0, 255, 16, 128);border-radius:50;")
        self.mainLayout.addWidget(self.label_avatar, 0, QtCore.Qt.AlignHCenter)

        self.spacer_1 = QtWidgets.QLabel(self)
        self.spacer_1.setMaximumHeight(40)
        self.spacer_1.setMinimumHeight(40)
        self.mainLayout.addWidget(self.spacer_1)

        self.input_uid = QtWidgets.QLineEdit(self)
        self.input_uid.setPlaceholderText("输入账号")
        self.input_uid.setAttribute(QtCore.Qt.WA_MacShowFocusRect, 0)
        self.input_uid.setMinimumSize(QtCore.QSize(185, 40))
        self.input_uid.setMaximumSize(QtCore.QSize(185, 40))
        font = QFont("微软雅黑")
        font.setPointSize(12)
        font.setWordSpacing(2)
        self.input_uid.setFont(font)
        self.input_uid.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.input_uid.setStyleSheet("""QLineEdit{
                                         background: transparent;
                                         border-width:0; 
                                         border-style:outset;
                                         border-bottom: 1px solid grey;
                                     }""")
        self.mainLayout.addWidget(self.input_uid, 0, QtCore.Qt.AlignHCenter)

        self.input_password = QtWidgets.QLineEdit(self)
        self.input_password.setPlaceholderText("输入密码")
        self.input_password.setAttribute(QtCore.Qt.WA_MacShowFocusRect, 0)
        self.input_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.input_password.setMinimumSize(QtCore.QSize(185, 40))
        self.input_password.setMaximumSize(QtCore.QSize(185, 16777215))
        self.input_password.setFont(font)
        self.input_password.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.input_password.setStyleSheet("""QLineEdit{
                                         background: transparent;
                                         border-width:0; 
                                         border-style:outset;
                                         border-bottom: 1px solid grey;
                                     }""")
        self.btn_login = IconButton('login', 30, 0.7)
        action = QWidgetAction(self.input_password)
        action.setDefaultWidget(self.btn_login)
        self.input_password.addAction(action, QLineEdit.TrailingPosition)
        self.mainLayout.addWidget(self.input_password, 0, QtCore.Qt.AlignHCenter)

        self.connect_info_label=QLabel(self)
        self.connect_info_label.setStyleSheet("color:red")
        # self.connect_info_label.setText("服务器未连接")
        self.mainLayout.addWidget(self.connect_info_label,0,QtCore.Qt.AlignHCenter)

        spacer_3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.mainLayout.addItem(spacer_3)

        self.layout_choice = QtWidgets.QHBoxLayout()
        self.layout_choice.setContentsMargins(20, 0, 0, 0)
        self.layout_choice.setSpacing(0)
        self.rBtn_save_password = QtWidgets.QRadioButton(self)
        self.rBtn_save_password.setAutoExclusive(False)
        self.rBtn_save_password.setText("记住密码")
        self.layout_choice.addWidget(self.rBtn_save_password)
        self.rBtn_auto_Login = QtWidgets.QRadioButton(self)
        self.rBtn_auto_Login.setAutoExclusive(False)
        self.rBtn_auto_Login.setText("自动登录")
        self.layout_choice.addWidget(self.rBtn_auto_Login)
        self.mainLayout.addLayout(self.layout_choice)

        # connect
        self.btn_exit.clicked.connect(lambda: self.quit_signal.emit())
        self.rBtn_auto_Login.toggled.connect(self.rbtn_set)
        self.rBtn_save_password.toggled.connect(self.rbtn_set)

    def rbtn_set(self):
        if self.sender() == self.rBtn_save_password and not self.rBtn_save_password.isChecked():
            self.rBtn_auto_Login.setChecked(False)
        if self.sender() == self.rBtn_auto_Login and self.rBtn_auto_Login.isChecked():
            self.rBtn_save_password.setChecked(True)

    def mouseMoveEvent(self, event: QMouseEvent):
        try:
            self._endPos = event.pos() - self._startPos
            self.move(self.pos() + self._endPos)
        except Exception as e:
            print(e)

    def mousePressEvent(self, event: QMouseEvent):

        try:
            if event.button() == QtCore.Qt.LeftButton:
                self._isTracking = True
                self._startPos = QtCore.QPoint(event.x(), event.y())
        except Exception as e:
            print(e)

    def mouseReleaseEvent(self, event: QMouseEvent):

        try:
            if event.button() == QtCore.Qt.LeftButton:
                self._isTracking = False
                self._startPos = None
                self._endPos = None
        except Exception as e:
            pass

    def connct_status(self,p_bool):
        if not p_bool:
            self.connect_info_label.setText("服务器未连接")
            self.btn_login.setEnabled(False)
        else:
            self.connect_info_label.setText("")
            self.btn_login.setEnabled(True)


    def login(self):
        uid=self.input_uid.text()
        password=self.input_password.text()
        if uid=='' or password=='':
            return



if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.setWindowFlag(Qt.Qt.FramelessWindowHint)
    login_window.show()
    sys.exit(app.exec_())
