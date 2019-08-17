import logging
import multiprocessing
import time

logging.basicConfig(
    level=logging.DEBUG, format='%(processName)s: %(message)s'
)


def f(num, arr):
    logging.debug(num)
    num.value += 1
    logging.debug(arr)  # 해당 데이터를 object를 형태로 가져온다
    for i in range(len(arr)):
        arr[i] *= 2


if __name__ == '__main__':
    num = multiprocessing.Value('f', 0)
    arr = multiprocessing.Array('i', [1, 2, 3, 4, 5])

    p1 = multiprocessing.Process(target=f, args=(num, arr))
    p2 = multiprocessing.Process(target=f, args=(num, arr))  # 2배되므로 배열은 4배, 2번 더하므로 2가된다

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    logging.debug(num.value)
    logging.debug(arr[:])
