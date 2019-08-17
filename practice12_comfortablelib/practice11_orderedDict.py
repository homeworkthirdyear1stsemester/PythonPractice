import collections

d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}  # 와전한 순서 보장을 안하고 있다 -> OrderedDic를 쓰면 보장됨
# print(d)
# d = collections.OrderedDict(d)
# print(d)

od = collections.OrderedDict(sorted(d.items(), key=lambda t: t[0]))  # 알파벳 순서로 정렬 -> 순서 정렬 가능
print(od)
