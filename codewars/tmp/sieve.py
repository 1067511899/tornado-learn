'''
Created on 2018年2月8日

@author: lenovo
'''
import time
import profile


def sieve(n):
    p = [True] * n
    for i in range(2, int(n ** .5) + 1):
        if p[i]:
            for j in range(i ** 2, n, i):
                p[j] = False
    result = []
    for x in range(2, n):
        if p[x]:
            result.append(x)
        
    return result


if __name__ == '__main__':
    beg = time.time()
# #     print(sieve(100))
    print(sieve(100000))
    print(time.time() - beg)
#     profile.run('sieve(100000)')
