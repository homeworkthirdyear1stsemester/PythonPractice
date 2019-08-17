import logging
import multiprocessing
import time

logging.basicConfig(level=logging.DEBUG, format='%(processName)s : %(message)s')


def worker1(i):
    logging.debug('start')
    time.sleep(5)
    logging.debug('end')

    return i * 2


if __name__ == '__main__':
    i = 10
    # t1 = multiprocessing.Process(target=worker1, args=(i,))
    with multiprocessing.Pool(3) as p:  # 무조건 pool 내부 숫자 개수 만큼 process 가 동시에 생성 된다
        # r = p.map(worker1, [100, 200])  # 해당 배열 개수 만큼 work1을 실행

        # logging.debug('executed apply')
        # logging.debug(r)  # 결과 또한 배열로 가져와짐

        # r = p.map_async(worker1, [100, 200])  # main thread 와도 따롤 실행
        # logging.debug(r.get())  # 결과 또한 배열로 가져와짐 -> main thread 가 대기해서 가져감
        r = p.imap(worker1, [100, 200])  # iterator형태로 실행
        logging.debug([i for i in r])  # 결과 또한 배열로 가져와짐 -> main thread 가 대기해서 가져감
