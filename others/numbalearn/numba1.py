from numpy import float64, zeros
from numpy.matlib import rand
import numba


@numba.jit
def matrix_multiply_jit(A, B):
    m, n = A.shape
    n, r = B.shape
    C = zeros((m, r), float64)
    for i in range(m):  
        for j in range(r):
            acc = 0
            for k in range(n):
                acc += A[i, k] * B[k, j]
            C[i, j] = acc
    return C


def matrix_multiply(A, B):
    m, n = A.shape
    n, r = B.shape
    C = zeros((m, r), float64)
    for i in range(m):  
        for j in range(r):
            acc = 0
            for k in range(n):
                acc += A[i, k] * B[k, j]
            C[i, j] = acc
    return C


n = 1000
A = rand(n, n)
B = rand(n, n)

from time import time
t1 = time()
matrix_multiply_jit(A, B)
t2 = time()
print(t2 - t1)
matrix_multiply(A, B)
t3 = time()
print(t3 - t2)
print((t3 - t2) / (t2 - t1))
