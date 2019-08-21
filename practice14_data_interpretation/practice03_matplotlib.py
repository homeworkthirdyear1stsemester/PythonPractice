import matplotlib.pyplot as plt
import numpy as np

plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()

plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.show()

plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')  # 선말 말고 다른 것도 추가한것
plt.axis([0, 6, 0, 10])
plt.show()

t = np.arange(0, 5, 0.2)
plt.plot(t, t, 'r--', t, t ** 2, 'bs', t, t ** 3, 'g^')
plt.show()

x = np.random.rand(50)
y = np.random.rand(50)
colors = np.random.rand(50)
area = np.random.rand(50) * 100
plt.scatter(x, y, s=area, c=colors, alpha=0.5)  # random 으로 화면에 찍어준 형태이다
plt.show()

objects = ['a', 'b', 'c', 'd', 'e', 'f']
y_pos = np.arange(len(objects))
value = [1, 2, 3, 4, 5, 6]

plt.bar(y_pos, value, alpha=0.5)  # 막대 그래프 형성 value -> y,
plt.xticks(y_pos, objects)
plt.ylabel('Usage')
plt.title('Title')  # title 형성
plt.show()

labels = ['python', 'C++', 'Ruby', 'Java']
sizes = [10, 20, 30, 40]
colors = ['red', 'green', 'yellow', 'blue']
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True)  # autopct 부동 소수점을 나타낼 때 사용한다
plt.axis('equal')  # 이것이 없을 경우 누워 있는 형태로 나타 나게 된다
plt.show()
