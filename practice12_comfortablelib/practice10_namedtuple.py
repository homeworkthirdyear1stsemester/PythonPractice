import collections
import csv

with open('anems.csv', 'w') as csvfile:
    filednames = ['first', 'last', 'address']
    writer = csv.DictWriter(csvfile, filednames=filednames)
    writer.writeheader()
    writer.writerows({'first': 'Mike', 'last': 'Jackson', 'address': 'A'})
    writer.writerows({'first': 'Jun', 'last': 'hi', 'address': 'B'})
    writer.writerows({'first': 'ab', 'last': 'aafsd', 'address': 'C'})

with open('name.csv', 'r') as f:
    csv_reader = csv.reader(f)
    Names = collections.namedtuple('Names', next(csv_reader))
    for row in csv_reader:
        names = Names._make(row)
        print(names.firstm, names.last, names.address)

# p = (10, 20)
# print(p[0])
#
# Point = collections.namedtuple('Point', ['x', 'y'])  # class 처럼 사용
# p = Point(x=10, y=20)  # x, y 는 튜플 처럼 값을 변 경 못함
# print(p.x)
#
# p1 = Point._make([100, 200])
# print(p1)  # 객체 출력
# print(p1._asdict())  # 튜플을 key value 형태로 반환
# p2 = p1._replace(x=500)
# print(p1)  # replace 하더라도 새로운 obj를 만듦
# print(p2)
#
#
# class SumPoint(collections.namedtuple('Point', ['x', 'y'])):  # 상속 형태로 가능 하다
#     @property  # 토탈 같은 걸 생성 할 수 있음
#     def total(self):
#         return self.x + self.y
#
#
# p3 = SumPoint(2, 3)
# print(p3.x, p3.y, p3.total)
