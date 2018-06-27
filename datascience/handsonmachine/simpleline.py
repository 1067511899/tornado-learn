import numpy as np
import matplotlib.pyplot as plt

X = np.array([[6], [8], [10], [14], [18]]).reshape(-1, 1)
y = [7, 9, 13, 17.5, 18] 
plt.figure()
plt.title('Pizza price plotted against diameter')
plt.xlabel('Diameter in inches')
plt.ylabel('Price in dollars')
plt.plot(X, y, 'k.')
plt.axis([0, 25, 0, 25])
from sklearn.linear_model import LinearRegression
model = LinearRegression()  # Create an instance of the estimator
model.fit(X, y)
test_pizza = np.array([[12]])
predicted_price = model.predict(test_pizza)[0]
print('A 12" pizza should cost: $%.2f' % predicted_price)
plt.plot(X, model.predict(X))
plt.scatter(X, model.predict(X), edgecolors='red')
plt.grid(True)
print(model.coef_, model.intercept_, 12 * model.coef_ + model.intercept_)
print('Residual sum of squares: %.2f' % np.mean((model.predict(X) - y) ** 2))
plt.show()
