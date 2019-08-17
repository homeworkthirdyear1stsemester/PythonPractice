import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s : %(message)s')


def worker1():
    logging.debug('start')
    time.sleep(5)
    logging.debug('end')


def worker2(x, y=1):
    print(threading.currentThread().getName(), 'start')  # logging 으로 args(tuple) 랑 kargs(dict) 형태 모두 넘겨 줄 수 있다
    logging.debug(x)
    logging.debug(y)
    time.sleep(5)
    print(threading.currentThread().getName(), 'end')


if __name__ == '__main__':
    t1 = threading.Thread(name='rename worker1', target=worker1)
    t2 = threading.Thread(target=worker2, args=(100,), kwargs={'y': 200})
    t1.start()  # thread 하나 시작
    t2.start()
    print('started')
