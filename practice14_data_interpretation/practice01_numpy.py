import numpy as np

a = np.array([1, 2, 3])
print(a)

print(a[1])

a = np.array([[1, 2, 3], [4, 5, 6]])
print(a)
print(a[0])

print(a.shape)  # 몇행 몇 열있는 지 알 수 있다
print(a.ndim)
print(a.dtype.name)  # data 탑입을 찾는다
print(a.size)
print(np.arange(0, 30, 5))  # 0이상 30 이하 까지 배열을 만들어준다 5만큼 차이
print(np.zeros((3, 4)))  # 3 4 배열 만들어준다
print(np.ones((3, 4), dtype=np.int16))
print(np.nan)
a = np.arange(24).reshape(2, 3, 4)
print(a)

x = np.arange(0, 10, 2)
y = np.arange(5)
z = np.arange(0, 100, 20)

print(np.append(x, y))

print(np.vstack([x, y, z]))  # 2차원 배열 형성 해 준다

print(np.hstack([x, y, z]))  # 1차원 배열로 연결 해줌
a = np.array([10, 20, 30, 40, 50, 60])
b = np.arange(5)
# a + b, a - b 등 연산 가능 a < number -> bool 형으로 실행 등도 가능

a = a.reshape(2, 3)
print(a)
print(a.T)  # col 과 low 를 바꿔준다
