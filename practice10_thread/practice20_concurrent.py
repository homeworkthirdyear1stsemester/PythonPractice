import concurrent.futures
import logging
import time

# logging.basicConfig(
#     level=logging.DEBUG, format='%(threadName)s: %(message)s'
# )
logging.basicConfig(
    level=logging.DEBUG, format='%(processName)s: %(message)s'
)


def worker(x, y):
    logging.debug('start')
    time.sleep(3)
    r = x * y
    logging.debug(r)
    logging.debug('end')

    return r


def main():
    # with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor: # thread 형태로 실행
    with concurrent.futures.ProcessPoolExecutor(max_workers=3) as executor:  # process 형태로 실행 -> 많은 코어를 응용할 경우
        # f1 = executor.submit(worker, 2, 5)
        # f2 = executor.submit(worker, 2, 5)
        # logging.debug(f1.result())
        # logging.debug(f2.result())
        # iterator 형태로 가져옴
        args = [[2, 2], [5, 5]]
        r = executor.map(worker, *args)
        logging.debug(r)
        logging.debug([i for i in r])


if __name__ == '__main__':
    main()
