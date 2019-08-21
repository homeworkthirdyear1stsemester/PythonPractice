import numpy as np
import pandas as pd

a = pd.Series([1, 2, np.nan])
print(a)  # 값을 볼 수 있다
print("sum :", a.sum())

df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
print(df)  # 가장 많이 사용함

print(df.dtypes)  # type 을 볼 수 있다

df = pd.DataFrame(np.random.randn(6, 4))
print(df)

df = pd.DataFrame(np.random.randn(6, 4), index=pd.date_range('20190101', periods=6))  # index 에 날짜가 형성 되어 있음
print(df)

print(df[0:3])  # 0 부터 3 직전까지 출력

print(df.iloc[0:2, 0:2])
print(df[df[1] > 0])

a = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20190101', periods=6))
print(a)

df[4] = a
print(df)  # a 가 추가된 것

print(df.shift(1))  # 한칸 옮기는 작업 공백일 경우 NaN가 나타난다

