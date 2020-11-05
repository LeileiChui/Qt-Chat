from queue import Queue


class MessageQueue:
    def __init__(self, chat_server):
        self.recv_buffer = Queue()
        self.chat_server = chat_server
        self.quit = False

    def run(self):
        while not self.chat_server.quit:
            if not self.recv_buffer.empty():
                send_pool, data_pack = self.recv_buffer.get()
                print(data_pack.type, data_pack.id)
                print("消息回复")
                if data_pack.type == 'login' or data_pack.type == 'logout':
                    self.chat_server.LoginService.data_buffer.append((send_pool, data_pack))
                if data_pack.type == 'msg':
                    send_pool.append(data_pack)
                send_pool.append(data_pack)
                self.recv_buffer.task_done()
