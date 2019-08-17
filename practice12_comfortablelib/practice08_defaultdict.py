import collections

# d = {}
l = ['a', 'a', 'a', 'b', 'b', 'c']
# for word in l:
#     if word not in d:
#         d[word] = 0
#     d[word] += 1

# for word in l:
#     d.setdefault(word, 0)  # d 에 해당 key 가 없으면 0으로 설정
#     d[word] += 1

d = collections.defaultdict(int)
for word in l:
    d[word] += 1
print(d)

d = collections.defaultdict(set)
s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), ('blue', 4)]

for k, v in s:
    d[k].add(v)

print(d)

c = collections.Counter()

for word in l:
    c[word] += 1
print(c)  # 자동으로 카운트 해준다
print(c.most_common(2))  # 최소 값이 2인 값인거만 출력
print(c.values())  # 값만 넣어줌

import re  # 정규표현

with open('practice08_defaultdict.py', 'r') as f:
    words = re.findall(r'\w+', f.read().lower())
    print(collections.Counter(words).most_common(20))

print(words)
