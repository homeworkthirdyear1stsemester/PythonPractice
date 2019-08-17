import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s : %(message)s')


def worker1():
    logging.debug('start')
    time.sleep(5)
    logging.debug('end')


def worker2():
    print(threading.currentThread().getName(), 'start')  # logging 으로 args(tuple) 랑 kargs(dict) 형태 모두 넘겨 줄 수 있다
    time.sleep(2)
    print(threading.currentThread().getName(), 'end')


if __name__ == '__main__':
    t1 = threading.Thread(target=worker1)
    t1.setDaemon(True)  # 해당 프로그램을 다른 프로그램이 기다리지 않고 끝낸다 -> t1이 아직 덜 끝나도 바로 종료
    t2 = threading.Thread(target=worker2)
    t1.start()  # thread 하나 시작
    t2.start()
    print('started')
    t1.join()  # 대기를 해야하는 것을 공표하는 것, 앵간하며 join으로 해하나다
    t2.join()  # t2을 기다리는 것 명시적으로 적어주는게 좋음 t2는 deamon thrread 가 아니므로 안 적어도되지만 가능
