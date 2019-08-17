import json
import pprint

l = ['apple', 'orange', 'banana', 'peach', 'mango']
l.insert(0, l[:])
# print(l)


pp = pprint.PrettyPrinter(indent=4, width=40, compact=True,
                          depth=3)  # 띄어쓰기 , 문자가 40개 까지 가능 ,depth : 3으로 하면 깊이가 최대 3 까지 만 출력 아니면 ...으로 출력
pp.pprint(l)

d = {'a': 'A', 'b': 'B', 'c': {'x': {'y': 'Y'}}}
print(json.dumps(d, indent=4))
