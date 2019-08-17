import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s : %(message)s')


def worker1(event):
    event.wait()  # 대기 상황으로 바뀜
    logging.debug('start')
    time.sleep(3)
    logging.debug('end')


def worker2(event):
    event.wait()
    logging.debug('start')
    time.sleep(3)
    logging.debug('end')


def worker3(event):  # set 이 다른 쓰레드에 정보를 넘겨 주는 형식
    logging.debug('start')
    logging.debug('end')
    event.set()  # 해당 barrier 가 wait 를 풀어준다


if __name__ == '__main__':
    event = threading.Event()
    t1 = threading.Thread(target=worker1, args=(event,))
    t2 = threading.Thread(target=worker2, args=(event,))
    t3 = threading.Thread(target=worker3, args=(event,))

    t1.start()  # thread 하나 시작
    t2.start()  # thread 하나 시작
    t3.start()  # thread 하나 시작
