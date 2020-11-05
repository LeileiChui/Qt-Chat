import socket
import threading

from PyQt5.QtWidgets import QWidget, QMessageBox

from Client import Client
from LoginWindow import LoginWindow
from ChatWindow import ChatWindow
from mainWindow import MainWindow


class ChatApp:
    def __init__(self):
        self.client = Client()
        self.login_window = LoginWindow(self)
        self.main_window = MainWindow(self)
        self.client.connect_info.connect(self.login_window.connct_status)
        self.login_window.quit_signal.connect(self.quit)
        self.client.login_result.connect(self.login_window.login_ack)

    def run(self):
        threading.Thread(target=self.client.run).start()

        self.login_window.show()

    def quit(self):
        try:
            self.login_window.hide()
            self.login_window.close()
            self.main_window.hide()
            self.main_window.close()
        except:
            pass
        self.client.quit = True
        exit(0)
