import matplotlib.pyplot as plt 
import seaborn as sns; sns.set() 
import numpy as np 

rng = np.random.RandomState(1) 
print(rng)
x = 10 * rng.rand(50) 
y = 2 * x - 5 + rng.randn(50) 
print(x)
print(type(x))
plt.scatter(x, y)

# plt.show()