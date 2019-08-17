import re

"""
match() 문자열 처음부터 정규식과 매치되는지 조사
search() 문자열 전체를 검색하여 정규식과 매치된느지 조사
findall() 정규식과 매치된느 모든 문자열을 리스트로 리턴
finditer() 정규식과 매치되는 모든 문자열을 iterator 객체로 리턴
"""

m = re.match('a.c', 'abc')  # .은 이의의 한 문자와 도일
print(m)  # 매치 하면 match obj 아니면 None 이 반환
print(m.group())  # 안에 내용 볼 수 있음

m = re.search('a.c', 'test abc test abc')  # 찾아서 검사함 처음 꺼만 해당
print(m)
print(m.span())  # 해당 문자열 위치
print(m.group())

m = re.findall('a.c', 'test abc test abc')  # 찾아서 검사함 처음 꺼만 해당
print(m)  # 해당 data 를 리스트로 반환

m = re.finditer('a.c', 'test abc test abc')  # 찾아서 검사함 처음 꺼만 해당
print(m)  # iterator 형태로 반환
print([w.group() for w in m])

m = re.match('ab?', 'a')  # b 0 ~ 1 일 경우
print(m)

m = re.match('ab*', 'a')  # b 가 0번 이상의 반복
print(m)

m = re.match('ab+', 'a')  # b가 한번이상 반복
print(m)

m = re.match('a{1, 3}b', 'aaab')  # a 가 3회 나와야 한다 -> 1~3개 사이 나와야한다
print(m)
m = re.match('[a-c]', 'a')  # a b c 사이 수를 입력 받아도됨
print(m)

m = re.match('\d', '123')  # 숫자일 경우 d 아무것도 없을 경우 w 를 넣는다
# 숫 자 이외의 것일 경우 d 대신에 D를 넣으면된다.
# 특수 문자 * ? 등등 일 경우는 역슬레시 \를 꼭 넣어줘야 한다
# 마지막 문자를 검사 할 경우 $ 표시를 뒤에 붙여준다
