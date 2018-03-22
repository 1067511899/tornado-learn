import numba as nb
import numpy as np
from time import time


@nb.vectorize([nb.float64(nb.float64, nb.float64)], target='parallel')
def asd3(x, y):
    return x + y


@nb.njit
def asd(x, y):
    return x + y


def asd2(x, y):
    return x + y


u = np.random.random((1000, 10))
w = np.random.random((1000, 10))

t1 = time()
print(t1)
asd(u, w)
t2 = time()
print(t2)
print(t2 - t1)
asd2(u, w)
t3 = time()
print(t3)
print(t3 - t2)
asd3(u, w)
t4 = time()
print(t4 - t3)

