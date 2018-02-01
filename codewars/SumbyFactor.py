'''
Given an array of positive or negative integers

I= [i1,..,in]

you have to produce a sorted array P of the form

[ [p, sum of all ij of I for which p is a prime factor (p positive) of ij] ...]

P will be sorted by increasing order of the prime numbers. The final result has to be given as a string in Java, C# or C++ and as an array of arrays in other languages.

Example:

I = [12, 15] # result = [[2, 12], [3, 27], [5, 15]]
[2, 3, 5] is the list of all prime factors of the elements of I, hence the result.

Notes: It can happen that a sum is 0 if some numbers are negative!

Example: I = [15, 30, -45] 5 divides 15, 30 and (-45) so 5 appears in the result, the sum of the numbers for which 5 is a factor is 0 so we have [5, 0] in the result amongst others.
'''
import math
global dic

dic = {}
def getp(n):
    tmp = int(math.sqrt(abs(n) + 1) + 1)
    m = n
    for x in range(2, tmp):
        if n % x == 0:
            dic[x] = dic.get(x, [])
            dic[x].append(m)
            n = n // x
    if n > tmp:
        dic[n] = dic.get(n, [])
        dic[n].append(m)
    return

def sum_for_list(lst):
    for y in lst:
        getp(y)
    
    key = sorted(list(dic.keys()))
    result = []
    for k in key:
        print(k, dic[k])
        result.append([k, sum(dic[k])])
    
    return result
# 某简洁答案，我的第二个测试没过，不知道原因。没能看到测试题。
def sum_for_list1(lst):
    factors = {i for k in lst for i in range(2, abs(k) + 1) if not k % i}
    prime_factors = {i for i in factors if not [j for j in factors - {i} if not i % j]}
    return [[p, sum(e for e in lst if not e % p)] for p in sorted(prime_factors)]


if __name__ == '__main__':
    a = [107, 158, 204, 100, 118, 123, 126, 110, 116, 100]
    print(sum_for_list(a))

