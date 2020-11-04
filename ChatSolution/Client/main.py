"""
@File: main.py
@time: 2020/11/3 6:11 上午
@Version: python3.8
@Author: Leilei Chui
@Contact: leilei.chui@gmail.com
@License: MIT Licence 
@Software: PyCharm
"""
import sys

from PyQt5.QtWidgets import QApplication, QMessageBox
from ChatApp import ChatApp

if __name__ == '__main__':
    app = QApplication(sys.argv)
    chat_app = ChatApp()
    chat_app.run()
    sys.exit(app.exec_())
