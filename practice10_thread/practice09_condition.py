import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s : %(message)s')


def worker1(condition):
    with condition:
        condition.wait()  # 대기 상황으로 바뀜
        logging.debug('start')
        time.sleep(3)
        logging.debug('end')


def worker2(condition):
    with condition:
        condition.wait()
        logging.debug('start')
        time.sleep(3)
        logging.debug('end')


def worker3(condition):  # set 이 다른 쓰레드에 정보를 넘겨 주는 형식
    with condition:
        logging.debug('start')
        logging.debug('end')
        condition.notifyAll()  # 해당 barrier 가 wait 를 풀어준다


if __name__ == '__main__':
    condition = threading.Condition()
    t1 = threading.Thread(target=worker1, args=(condition,))
    t2 = threading.Thread(target=worker2, args=(condition,))
    t3 = threading.Thread(target=worker3, args=(condition,))

    t1.start()  # thread 하나 시작
    t2.start()  # thread 하나 시작
    t3.start()  # thread 하나 시작
