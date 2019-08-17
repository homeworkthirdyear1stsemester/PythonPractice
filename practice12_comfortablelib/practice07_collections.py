import collections

a = {'a': 'a', 'c': 'c', 'num': 0}
b = {'b': 'b', 'c': 'cc'}
c = {'b': 'bbb', 'c': 'ccc'}


# print(a)
# a.update(b)  # b 에 값을 덮어 씌운다
# print(a)

# m = collections.ChainMap(a, b, c)
# print(m)
# print(m.maps)  # list 로 모든 정보를 저장
# print(m['c'])  # 처음부터 우선저긍로 출력 그러므로 c 가 출력됨
# m.maps.reverse()
# print(m.maps)
# print(m['c'])


class DeepCainMap(collections.ChainMap):
    def __setitem__(self, key, value):
        for mapping in self.maps:
            if type(mapping[key]) is int and mapping[key] < value:
                mapping[key] = value
            return
        self.maps[0][key] = value


m = DeepCainMap(a, b, c)
m['num'] = 1
print(m['num'])
