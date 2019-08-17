import queue
from multiprocessing.managers import BaseManager

queue = queue.Queue()


class QueueManager(BaseManager):
    pass


QueueManager.register(
    'get_queue', callable=lambda: queue
)  # 읽어 오는 함수를 등록함

manager = QueueManager(address=('127.0.0.1', 50000), authkey=b'abracadabra')
server = manager.get_server()
server.serve_forever()
