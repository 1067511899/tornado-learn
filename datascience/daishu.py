from numpy import *

A = mat([[1, 2, 4, 5, 7, ], [9, 12, 11, 8, 2, ], [6, 4, 3, 2, 1, ], [9, 1, 3, 4, 5, ], [0, 2, 3, 4, 1]])

AT = A.T

print(A * AT)

A = [8, 1, 6]
normA = linalg.norm(A)
print(normA)
