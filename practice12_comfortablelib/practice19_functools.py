import functools


def d(f):
    @functools.wraps(f)  # f 함수에서의 doc 를 출력 해준다
    def w():
        """ Wrapper docstring """
        print('decorator')
        return f()

    return w


@d
def example():
    """ Example docstring """
    print('example')


# print(example.__doc__)
help(example)


def task(f):
    print('start')
    print(f())


def f(x, y):
    return x + y


p = functools.partial(f, 10, 20)
task(p)  # 이미 있는 이수를 널어 주는 역할으 한다
# task(lambda x, y: x + y)
