import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s : %(message)s')


def worker1(lock):
    with lock:
        logging.debug('start')
        time.sleep(5)
        logging.debug('end')


def worker2(lock):
    with lock:
        logging.debug('start')
        time.sleep(5)
        logging.debug('end')


def worker3(lock):
    with lock:
        logging.debug('start')
        time.sleep(5)
        logging.debug('end')


if __name__ == '__main__':
    semaphore = threading.Semaphore(2)  # 들어올 수 있는 thread 수를 나타내는 것 lock 개수를 설정 할 수 있다
    t1 = threading.Thread(target=worker1, args=(semaphore,))
    t2 = threading.Thread(target=worker2, args=(semaphore,))
    t3 = threading.Thread(target=worker2, args=(semaphore,))
    t1.start()  # thread 하나 시작
    t2.start()
    t3.start()
