import matplotlib.pyplot as plt  # import matplotlib
import numpy as np
import math

# x = []
# for i in range(-100, 110, 1):
#     x.append(i / 10)
x = np.linspace(-100, 100, 100)  #
# x = np.arange(-100, 100, 0.1)
# x = np.array(x)
# y = x ** 3 - 6 * (x ** 2) + 9 * x
y = np.exp(x) / np.sum(np.exp(x))
plt.axis([-1, 1, -1, 1])

ax = plt.axes()
# a = [-10, 10]
# b = [-16, -16]
# plt.plot(a, b)
# spine placement data centered
ax.spines['left'].set_position(('data', 0.0))
ax.spines['bottom'].set_position(('data', 0.0))
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
# plt.figure()  # Create a new figure
plt.plot(x, y)
# y = 2 ** x
# plt.plot(x, y)
# a = np.linspace(0, 100, 100)  #
# b = math.log10(x)
# plt.plot(a, b)

# 
# plt.plot(x, x * 0)
# plt.plot(x * 0, x)
# plt.plot(x, -4 * x)

plt.show()
# print(math.exp(10))
