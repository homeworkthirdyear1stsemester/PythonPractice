print('s')
print(str('s'))
print(repr('s'))

import datetime

d = datetime.datetime.now()
print(d)
print(str(d))
print(repr(d))  # repr 로 형태로 지정

print('{!r} {} {!s}'.format('test', 'test1', 'test2'))  # !r : 리프리젠테이션


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point<object>'

    def __str__(self):
        return 'Point ({}, {})'.format(self.x, self.y)


p = Point(10, 200)
print('{0!r}'.format(p))
print('{0}'.format(p))
