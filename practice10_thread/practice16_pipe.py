import logging
import multiprocessing
import time

logging.basicConfig(
    level=logging.DEBUG, format='%(processName)s: %(message)s'
)


def f(conn):
    conn.send(['test'])
    time.sleep(5)
    conn.close()


if __name__ == '__main__':
    parent_conn, child_conn = multiprocessing.Pipe()
    p = multiprocessing.Process(target=f, args=(parent_conn,))
    p.start()
    p.join()  # 대기 하고 받음
    logging.debug(child_conn.recv())  # 만약 아무 것도 없으면 받을 때 까지 대기한다
