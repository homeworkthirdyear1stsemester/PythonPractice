import logging
import threading

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s : %(message)s')


def worker1(d, lock):
    logging.debug('start')
    lock.acquire()
    i = d['x']
    d['x'] = i + 1  # 공유 변수
    logging.debug(d)
    lock.release()
    logging.debug('end')


def worker2(d, lock):
    print(threading.currentThread().getName(), 'start')  # logging 으로 args(tuple) 랑 kargs(dict) 형태 모두 넘겨 줄 수 있다
    with lock:  # 이렇게 사용해도된다
        i = d['x']
        d['x'] = i + 1
        logging.debug(d)
        with lock:
            d['x'] = i + 1  # 이렇게 되면 프로그램이 끝나지 않음 데드 락이 생김
            # 이럴 경우 RLock를 하면된다 -> nested lock 를 가능하게한다
    print(threading.currentThread().getName(), 'end')


if __name__ == '__main__':
    d = {'x': 0}
    lock = threading.RLock()
    t1 = threading.Thread(target=worker1, args=(d, lock))
    t2 = threading.Thread(target=worker2, args=(d, lock))
    t1.start()  # thread 하나 시작
    t2.start()
