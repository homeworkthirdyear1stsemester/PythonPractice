import contextlib


# def tag(name):
#     def _tag(f):
#         def _wrapper(content):
#             print('<{}>'.format(name))
#             r = f(content)
#             print('</{}>'.format(name))
#             return r
#
#         return _wrapper
#
#     return _tag
#
#
# @tag('h2')
# def f(content):
#     print(content)
#
#
# # f = tag('h2')(f)
# f('test')


@contextlib.contextmanager  # yield 로 권한 전환
def tag(name):
    print('<{}>'.format(name))
    yield  # 주도권을 넘겨준다
    print('</{}>'.format(name))


@tag('h2')
def f(content):
    print(content)


f('test')

with tag('h2'):  # 위와 똑같은 결과를 얻는다 -> @tag 말고 다른 방식으로 할 수도 있다.
    print('test')
