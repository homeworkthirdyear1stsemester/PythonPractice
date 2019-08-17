import collections
import queue

q = queue.Queue()
lq = queue.LifoQueue()  # [1,2,3] 이런 큐가 있으면 3부터 꺼냄 stack 와 비슷
l = []
d = collections.deque()  # list 와 차이점 메모리 관계상 list 보다 우수, 속도도 우수

for i in range(3):
    q.put(i)
    lq.put(i)
    l.append(i)
    d.append(i)

# for _ in range(3):
#     print('FIFO queue = {}'.format(q.get()))
#     print('LIFO queue = {}'.format(lq.get()))
#     print('list       = {}'.format(l.pop(0)))  # queue 처럼 쓸려면 0 을 index 로 넣어야함
#     print('dequeue    = {}'.format(d.popleft()))  # popleft 할 경우 queue와 동일
#     print()

d.extend('x')  # 제일 뒤에 추가
# d.rotate()  # 몇칸씩 돌린다
print(d)
