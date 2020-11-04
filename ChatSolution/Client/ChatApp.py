import socket
import threading

from PyQt5.QtWidgets import QWidget, QMessageBox

from Client import Client
from LoginWindow import LoginWindow
class ChatApp:
    def __init__(self):
        self.client=Client()
        self.login_window=LoginWindow()
        self.main_window=QWidget()
        self.client.connect_info.connect(self.login_window.connct_status)
        self.login_window.quit_signal.connect(self.quit)

    def login_ack(self,p_data_pack):
        if p_data_pack.ack_data.login_status:
            self.login_window.hide()
            self.main_window.show()
        else:
            self.login_window.input_password.clear()
            QMessageBox.warning(self,title="错误",text="登陆失败")

    def run(self):
        threading.Thread(target=self.client.run).start()

        self.login_window.show()

    def quit(self):
        self.login_window.hide()
        self.client.quit=True
        exit(0)