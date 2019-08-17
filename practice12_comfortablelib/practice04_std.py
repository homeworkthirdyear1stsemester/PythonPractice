import contextlib
import logging
import sys

# x = input('Enter: ')
# print(x)
#
# for line in sys.stdin:  # input 보다 더 낮은 level 로서 실행
#     print(line)

# with open('stdout.log', 'w') as f:  # 파일에 작성
#     with contextlib.redirect_stdout(f):
#         help(sys.stdout)

# print('hello')
# sys.stdout.write('hello')

with open('stderr.log', 'w') as f:  # logging 정보가 해당 파일에 저장 되게 된다
    with contextlib.redirect_stderr(f):
        logging.error('Error!')

# logging.error('Error!')  # 항상 stderr 를 하도록 되어있다
# sys.stderr.write('Error!')
