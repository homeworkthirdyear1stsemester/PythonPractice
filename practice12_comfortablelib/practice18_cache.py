def memoize(f):
    memo = {}

    def _wrapper(n):
        if n not in memo:
            memo[n] = f(n)
            print('hit')
        return memo[n]

    return _wrapper


import functools


# @memoize  # 해당 함수를 먼저 인자에 넘겨서 실행한다.
@functools.lru_cache()  # 캐쉬를 설정하는 것 maxsize 를 설정 할 수 있다
def long_func(n):
    r = 0
    for i in range(10000000):
        r += n * i
    return r


for i in reversed(range(10)):
    print(long_func(i))

print(long_func.cache_info())

for i in range(10):
    print(long_func(i))
