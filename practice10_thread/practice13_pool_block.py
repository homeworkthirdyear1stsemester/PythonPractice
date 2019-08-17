import logging
import multiprocessing
import time

logging.basicConfig(level=logging.DEBUG, format='%(processName)s : %(message)s')


def worker1(i):
    logging.debug('start')
    time.sleep(5)
    logging.debug('end')

    return i


if __name__ == '__main__':
    i = 10
    # t1 = multiprocessing.Process(target=worker1, args=(i,))
    with multiprocessing.Pool(3) as p:  # 무조건 pool 내부 숫자 개수 만큼 process 가 동시에 생성 된다
        logging.debug(p.apply(worker1, (200,)))  # 미리 먼저 처리 한 후에 다른 것을 실행
        logging.debug('executed apply')
        p1 = p.apply_async(worker1, (100,))  # 비동기 병렬화
        p2 = p.apply_async(worker1, (100,))

        logging.debug(p1.get())  # 해당 p1의 실행 후 1초안에 결과가 안 나오면 에러를 나타내 주라고 한다
        logging.debug(p2.get())  # 해당 결과를 반환 받음
