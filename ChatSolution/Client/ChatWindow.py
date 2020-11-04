# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chat_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys
import time

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QWidget, QListView, QMainWindow, QApplication
from PyQt5.QtGui import QStandardItemModel, QStandardItem


class ObjectMessageUi(object):

    def setupUi(self, QWidget):
        self.horizontalLayout = QtWidgets.QHBoxLayout(QWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.headerP = QtWidgets.QLabel()
        self.headerP.setMinimumSize(QtCore.QSize(70, 60))
        self.headerP.setMaximumSize(QtCore.QSize(70, 60))
        self.headerP.setStyleSheet("background:rgb(255, 0, 0);\n"
"border-radius:30")
        self.headerP.setText("")
        self.headerP.setObjectName("headerP")
        self.horizontalLayout.addWidget(self.headerP)
        self.message_label = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.message_label.setFont(font)
        self.message_label.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.message_label.setObjectName("message_label")
        self.horizontalLayout.addWidget(self.message_label)

        self.retranslateUi(QWidget)

    def retranslateUi(self, QWidget):
        _translate = QtCore.QCoreApplication.translate
        self.message_label.setText(_translate("MainWindow", "hello!!!!!!!!"))


class SelfMessageUi(object):
    def setupUi(self, QWidget):
        self.horizontalLayout = QtWidgets.QHBoxLayout(QWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.headerP = QtWidgets.QLabel()
        self.headerP.setMinimumSize(QtCore.QSize(70, 60))
        self.headerP.setMaximumSize(QtCore.QSize(70, 60))
        self.headerP.setStyleSheet("background:rgb(255, 0, 0);\n"
                                   "border-radius:30")
        self.headerP.setText("")
        self.headerP.setObjectName("headerP")
        self.message_label = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.message_label.setFont(font)
        self.message_label.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.message_label.setObjectName("message_label")
        self.message_label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.horizontalLayout.addWidget(self.message_label)
        self.horizontalLayout.addWidget(self.headerP)
        self.retranslateUi(QWidget)

    def retranslateUi(self, QWidget):
        _translate = QtCore.QCoreApplication.translate
        self.message_label.setText(_translate("MainWindow", "hi!!!!!!!!"))



class ObjMessage(QWidget):
    def __init__(self,message_pak=''):
        super(ObjMessage, self).__init__()
        self.ui = ObjectMessageUi()
        self.ui.setupUi(self)
        if len(message_pak)!=0:
            pass#TODO


class SelfMessage(QWidget):
    def __init__(self,message_pak=''):
        super(SelfMessage, self).__init__()
        self.ui = SelfMessageUi()
        self.ui.setupUi(self)
        if len(message_pak)!=0:
            self.ui.message_label.setText(str(message_pak))


class InfoItemUi(object):
    def setupUi(self, list_item):
        list_item.setObjectName("list_item")
        list_item.setMaximumSize(200,70)
        list_item.setMinimumSize(200,70)
        list_item.setStyleSheet("background:rgb(255, 255, 255)")
        self.horizontalLayout = QtWidgets.QHBoxLayout(list_item)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(list_item)
        self.widget.setMinimumSize(QtCore.QSize(70, 0))
        self.widget.setMaximumSize(QtCore.QSize(70, 70))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.delete_2 = QtWidgets.QPushButton(self.widget)
        self.delete_2.setStyleSheet("border:none")
        self.delete_2.setMinimumSize(QtCore.QSize(15, 70))
        self.delete_2.setMaximumSize(QtCore.QSize(15, 70))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.delete_2.setFont(font)
        self.delete_2.setObjectName("delete_2")
        self.horizontalLayout_2.addWidget(self.delete_2)
        self.headPic = QtWidgets.QLabel(self.widget)
        self.headPic.setMinimumSize(QtCore.QSize(50, 50))
        self.headPic.setMaximumSize(QtCore.QSize(50, 50))
        self.headPic.setStyleSheet("border-radius:20px;\n"
                                   "background:rgb(0, 0, 0)rgb(255, 255, 255)rgb(161, 161, 161);\n"
                                   "")
        self.headPic.setText("")
        self.headPic.setObjectName("headPic")
        self.horizontalLayout_2.addWidget(self.headPic)
        self.horizontalLayout.addWidget(self.widget)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.nickname = QtWidgets.QLabel(list_item)
        self.nickname.setMinimumSize(QtCore.QSize(425, 35))
        self.nickname.setMaximumSize(QtCore.QSize(425, 25))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.nickname.setFont(font)
        self.nickname.setObjectName("nickname")
        self.verticalLayout.addWidget(self.nickname)
        self.snapshot = QtWidgets.QLabel(list_item)
        self.snapshot.setMinimumSize(QtCore.QSize(425, 20))
        self.snapshot.setMaximumSize(QtCore.QSize(425, 25))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(10)
        self.snapshot.setFont(font)
        self.snapshot.setStyleSheet("color:#5B5B5B")
        self.snapshot.setObjectName("snapshot")
        self.verticalLayout.addWidget(self.snapshot)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(list_item)
        QtCore.QMetaObject.connectSlotsByName(list_item)

    def retranslateUi(self, list_item):
        _translate = QtCore.QCoreApplication.translate
        list_item.setWindowTitle(_translate("list_item", "Form"))
        self.delete_2.setText(_translate("list_item", "X"))
        self.nickname.setText(_translate("list_item", "群聊助手"))
        self.snapshot.setText(_translate("list_item", "message"))


class InfoItem(QWidget):
    def __init__(self):
        super(InfoItem, self).__init__()
        self.ui = InfoItemUi()
        self.ui.setupUi(self)

class ChatWindowUi(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(1000, 565)
        Widget.setWindowOpacity(1.0)
        Widget.setStyleSheet("")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.infoItemList = MessageListView()
        self.infoItemList.setMaximumSize(QtCore.QSize(200, 16777215))
        self.infoItemList.setObjectName("infoItemList")
        self.horizontalLayout.addWidget(self.infoItemList)
        self.widget = QtWidgets.QWidget(Widget)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.messageWindow = MessageListWindow(self)
        self.messageWindow.setObjectName("messageWindow")
        self.verticalLayout.addWidget(self.messageWindow)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.messageInput = QtWidgets.QLineEdit(self.widget)
        self.messageInput.setObjectName("messageInput")
        self.horizontalLayout_2.addWidget(self.messageInput)
        self.send = QtWidgets.QPushButton(self.widget)
        self.send.setObjectName("send")
        self.horizontalLayout_2.addWidget(self.send)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addWidget(self.widget)

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.send.setText(_translate("Widget", "发送"))

    # def update_chatWindow(self):


class MessageListView(QListView):
    def __init__(self):
        super(MessageListView, self).__init__()
        self._model = QStandardItemModel(self)
        self.setModel(self._model)

        for i in range(5):
            item = QStandardItem()
            self._model.appendRow(item)

            index = self._model.indexFromItem(item)
            widget = InfoItem()
            widget.ui.snapshot.setText("信息" + str(i))
            widget.ui.delete_2.clicked.connect(self.remove)
            widget.ui.delete_2.setProperty("item", item)
            # widget.ui.horizontalLayout.clicked.connect(self.switch)

            item.setSizeHint(QSize(190, 70))
            self.setIndexWidget(index, widget)

    def update_list(self):
        pass  # TODO

    def remove(self):
        item = self.sender().property("item")
        index = self._model.indexFromItem(item).row()
        self._model.removeRow(index)

    def swtich(self):
        pass


class MessageListWindow(QListView):
    def __init__(self, chat_window):
        super(MessageListWindow, self).__init__()
        self._model = QStandardItemModel(self)
        self.setModel(self._model)

        for i in range(5):
            item = QStandardItem()
            self._model.appendRow(item)

            index = self._model.indexFromItem(item)
            if i % 2 == 0:
                widget = ObjMessage()
            else:
                widget = SelfMessage()
            print(widget.sizeHint())
            item.setSizeHint(widget.sizeHint())

            self.setIndexWidget(index, widget)


class ChatWindow(QWidget):
    def __init__(self,app):
        super(ChatWindow, self).__init__()
        self.ui = ChatWindowUi()
        self.ui.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    chatwindow = ChatWindow(app)
    chatwindow.show()
    sys.exit(app.exec_())

