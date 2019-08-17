import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s : %(message)s')


def worker1(x, y=1):
    logging.debug('start')
    logging.debug(x)
    logging.debug(y)
    time.sleep(5)
    logging.debug('end')


def worker2():
    print(threading.currentThread().getName(), 'start')  # logging 으로 args(tuple) 랑 kargs(dict) 형태 모두 넘겨 줄 수 있다
    time.sleep(2)
    print(threading.currentThread().getName(), 'end')


if __name__ == '__main__':
    t = threading.Timer(3, worker1, args=(100,), kwargs={'y': 200})
    t.start()
    # 3 초 뒤에 실행
