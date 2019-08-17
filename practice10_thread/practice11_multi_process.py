from multiprocessing import (
    Process,
    Lock, RLock, Semaphore, Queue, Event, Condition, Barrier,
    Value, Pipe, Manager, Array)  # Thread에 존재 하는 것이 멀티 프로스에도 존재함 3번째 줄은 공유 변수 관련 라이브러리 이다

import logging
import multiprocessing

logging.basicConfig(level=logging.DEBUG, format='%(processName)s : %(message)s')


def worker1(i):
    logging.debug('start')
    logging.debug(i)
    logging.debug('end')


def worker2(i):
    logging.debug('start')
    logging.debug(i)
    logging.debug('end')


if __name__ == '__main__':
    i = 10
    t1 = multiprocessing.Process(target=worker1, args=(i,))
    t1.daemon = True
    t2 = multiprocessing.Process(target=worker2, args=(i,))
    t1.start()  # thread 하나 시작
    t2.start()

    t1.join()  # t1 프로세스를 대기
