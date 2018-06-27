from sklearn import linear_model
import matplotlib.pyplot as plt 
from sklearn import tree
# import numpy as np
# from sklearn.ensemble import BaggingRegressor
# model = BaggingRegressor()
# model = tree.DecisionTreeRegressor()
model = linear_model.LinearRegression()

X = [[1.01], [0.49], [0.31], [1.51], [0.37], [0.73], [1.53], [0.56],
         [0.41], [0.74], [0.63], [0.6], [2.06], [1.1], [1.31]]
y = [7366, 985, 544, 9140, 493, 3011, 11413, 1814,
         876, 2690, 1190, 4172, 11764, 4682, 6172]

plt.scatter(X, y)

model.fit(X, y)
result = model.predict(X)
plt.plot(X, model.intercept_ + model.coef_ * X, color='red', linewidth='3')
# plt.plot(X, result, 'ro-', label='predict value')
plt.show()

