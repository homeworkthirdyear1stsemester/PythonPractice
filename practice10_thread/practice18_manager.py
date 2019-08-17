import logging
import multiprocessing
from multiprocessing import Manager  # 속도가 느리다는 결점이 있음

logging.basicConfig(level=logging.DEBUG, format='%(processName)s: %(message)s')


def worker1(l, d, n):
    l.reverse()
    d['x'] += 1
    n.y += 1


if __name__ == '__main__':
    with Manager() as manager:
        l = manager.list()  # 전부 manager 로 했기 때문에 공유 변수로 사용 할 수 있다
        d = manager.dict()
        n = manager.Namespace()

        l.append(1)
        l.append(2)
        l.append(3)
        d['x'] = 0
        n.y = 0

        p1 = multiprocessing.Process(target=worker1, args=(l, d, n))
        p2 = multiprocessing.Process(target=worker1, args=(l, d, n))

        p1.start()
        p2.start()

        p1.join()
        p2.join()

        logging.debug(l)
        logging.debug(d)
        logging.debug(n)
