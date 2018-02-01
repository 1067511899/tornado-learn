'''
Given a positive number n > 1 find the prime factor decomposition of n. The result will be a string with the following form :

 "(p1**n1)(p2**n2)...(pk**nk)"
with the p(i) in increasing order and n(i) empty if n(i) is 1.

Example: n = 86240 should return "(2**5)(5)(7**2)(11)"
'''
import collections
import math
def primeFactors(n):
    dic = collections.OrderedDict()
    for x in range(2, int(math.sqrt(n + 1) + 1)):
        while 1:
            if n % x == 0:
                dic[x] = dic.get(x, 0) + 1
                n = n // x
            else:
                break
    result = ''
    if n > 2:
        dic[n] = dic.get(n, 0) + 1
    if len(dic) == 0:
        return '({})'.format(n)
    keys = list(dic.keys())
    for key in keys:
        if dic[key] > 1:
            result += '({}**{})'.format(key, dic[key])
        else:
            result += '({})'.format(key)
    return result

# 看不懂。。。。。。。
def primeFactors1(n):
    i, j, p = 2, 0, []
    while n > 1:
        while n % i == 0: n, j = n / i, j + 1
        if j > 0: p.append([i, j])
        i, j = i + 1, 0
    return ''.join('(%d' % q[0] + ('**%d' % q[1]) * (q[1] > 1) + ')' for q in p)

if __name__ == '__main__':
    print(primeFactors(7775460))
