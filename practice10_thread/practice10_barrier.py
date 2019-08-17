import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s : %(message)s')


def worker1(barrier):
    r = barrier.wait()  # 대기 상황으로 바뀜
    logging.debug('name={}'.format(r))
    while True:
        logging.debug('start')
        time.sleep(2)
        logging.debug('end')


def worker2(barrier):
    r = barrier.wait()  # 대기 상황으로 바뀜
    logging.debug('name={}'.format(r))
    while True:
        logging.debug('start')
        time.sleep(2)
        logging.debug('end')


if __name__ == '__main__':
    barrier = threading.Barrier(2)  # barrier 의 value 가 0이 될때 까지 wait 를 걸면 대기 한다 그리고 0이되면 모든 Thread가 같이 실행한다
    t1 = threading.Thread(target=worker1, args=(barrier,))
    t2 = threading.Thread(target=worker2, args=(barrier,))

    t1.start()  # thread 하나 시작
    t2.start()  # thread 하나 시작

# worker1이 server 고 worker2가 client 가 될 떄 사용 한다
