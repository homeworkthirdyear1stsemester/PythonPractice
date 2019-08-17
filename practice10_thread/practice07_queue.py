import logging
import queue
import threading

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s : %(message)s')


def worker1(queue):
    logging.debug('start')
    while True:
        item = queue.get()
        if item is None:
            break
        logging.debug(item)
        queue.task_done()  # 10번 데이터를 넣었으므로 10번 task_done 이 불려지지 않으면 무한 대기로 넘어간다

    logging.debug('end')


if __name__ == '__main__':
    queue = queue.Queue()
    for i in range(100000):
        queue.put(i)

    ts = []
    for _ in range(3):
        t1 = threading.Thread(target=worker1, args=(queue,))
        t1.start()  # thread 하나 시작
        ts.append(t1)
    # t2 = threading.Thread(target=worker2, args=(queue,))
    # t2.start()

    logging.debug('tasks are not done')
    queue.join()  # queue 의 작업이 모두 끝날때 까지 대기
    logging.debug('task are done')

    for _ in range(3):
        queue.put(None)

    [t.join() for t in ts]
