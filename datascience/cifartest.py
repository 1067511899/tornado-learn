from sklearn import linear_model
import matplotlib.pyplot as plt 
# import seaborn as sns; sns.set() 
# import numpy as np 

clf = linear_model.LinearRegression()
# clf.fit ([[1.01, 7366], [0.49, 985], [0.31, 544], [1.51, 9140], [0.37, 493], [0.73, 3011], [1.53, 11413]], [0, 7, 3])
# dia_X = np.array([1.01, 0.49, 0.31, 1.51, 0.37, 0.73, 1.53])
dia_X = [[1.01], [0.49], [0.31], [1.51], [0.37], [0.73], [1.53], [0.56],
         [0.41], [0.74], [0.63], [0.6], [2.06], [1.1], [1.31]]
# dia_Y = [[7366], [985], [544], [ 9140], [ 493], [ 3011], [ 11413]]
# dia_X = [[1.01, 7366], [0.49, 985], [0.31, 544], [1.51, 9140], [0.37, 493], [0.73, 3011], [1.53, 11413]]
dia_Y = [7366, 985, 544, 9140, 493, 3011, 11413, 1814,
         876, 2690, 1190, 4172, 11764, 4682, 6172]

plt.scatter(dia_X, dia_Y)
print(dia_X)
clf.fit(dia_X, dia_Y)
print(clf.coef_)
print(clf.intercept_)
print('%d x %d ' % (clf.coef_, clf.intercept_))
plt.show()

# 1.1 4,682
# 1.31 6,172
