import contextlib


def is_ok_job():
    try:
        print('do something')
        # raise Exception
        return True
    except:
        return False


def cleanup():
    print('clean up')


# try:
#     is_ok = is_ok_job()
#     print('more task')
# finally:
#     if not is_ok:
#         cleanup()

def cleanup2():
    print('clean up 2')


with contextlib.ExitStack() as stack:  # 위와 동일한 코드
    stack.callback(cleanup)  # finally 와 동일하다
    stack.callback(cleanup2)


    @stack.callback
    def cleanup3():  # 무조건 stack 에 적제 된다
        print('clean up 3')


    is_ok = is_ok_job()
    print('more task')

    if is_ok:
        stack.pop_all()  # 해주기 싫을 경우 stack 에서 모두 제거
