import re

s = 'My name is ... Mike'
print(s.split())

p = re.compile(r'\W+')  # 영문자 외에 값이 므로 ... 같이 특수문자는 제외
print(p.split(s))  # split 랑 동일

# 치환

p = re.compile('(blue|white|red)')
print(p.sub('colour', 'blue socks and red shoes', count=1))

# Greedy

s = '<html><head><title>Title</title></head></html>'

print(re.match('<.*?>', s))  # 마지막이 아닌 처음 만나는 것을 판별 하는 것
