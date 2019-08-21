import matplotlib.pyplot as plt
import pandas as pd

import sklearn.datasets
import sklearn.linear_model
import sklearn.model_selection

boston = sklearn.datasets.load_boston()
X = boston.data
df = pd.DataFrame(boston.data, columns=boston.feature_names)
print(df)

y = boston.target
print(y)  # 주택 가격

X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.2)
lr = sklearn.linear_model.LinearRegression()
lr.fit(X_train, y_train)
print(lr.score(X_test, y_test))

predicted = lr.predict(X)  # 예 측정보
flg, ax = plt.subplots()
ax.scatter(y, predicted, edgecolors=(0, 0, 0))
ax.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=4)
ax.set_xlabel('Measured')
ax.set_ylabel('Predicted')
plt.show()
