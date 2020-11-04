from queue import Queue


class MessageQueue:
    def __init__(self):
        self.recv_buffer = Queue()
        self.quit = False

    def run(self):
        while not self.quit:
            if not self.recv_buffer.empty():
                send_pool, data_pack = self.recv_buffer.get()
                print(data_pack.type, data_pack.id)
                print("消息回复")
                if data_pack.type=='login'
                send_pool.append(data_pack)
                self.recv_buffer.task_done()

