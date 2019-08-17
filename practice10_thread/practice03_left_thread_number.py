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
    # threads = []
    for _ in range(5):
        t1 = threading.Thread(target=worker1)
        t1.setDaemon(True)  # 해당 프로그램을 다른 프로그램이 기다리지 않고 끝낸다 -> t1이 아직 덜 끝나도 바로 종료
        t1.start()  # thread 하나 시작
        # threads.append(t1)
    for thread in threading.enumerate():
        if thread is threading.currentThread(): # main thread
            print(thread)
            continue
        thread.join()
