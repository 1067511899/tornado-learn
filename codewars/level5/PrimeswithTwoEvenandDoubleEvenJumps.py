'''
Think in all the primes that: if p is prime and p < n , all these following numbers (p + 2) , (p + h) and (p + 2h) are all primes, being h an even number such that: 2 <= h <= hMax

Your function, give_max_h() , will receive 2 arguments n and hMax .

It should find for which value or values of h , we encounter the maximum amount of primes that satisfy the above constraint, testing for all possible even values from 2 to hMax included.

So, give_max_h(n, hMax) should ouput a list of lists with the following structure: a) if you find a unique solution:

[[h0, max amount of primes]] being h0 such that 2 <= h0 <= hMax and is the value that has the highest amount of collected primes

b) if you have more than one solution, suposse 2 , you found two values of h: h0 , h1 such that : 2 <= ho < h1 <= hmax

[[h0, max_amount_of_primes], [h1, max_amount_of_primes]] (lists should be sorted by the value of h) Let's see some cases: For Python and Ruby:

Case 1
give_max_h(30, 8) ------> [[6, 3]]
For Javascript:

Case 1
giveMax_h(30, 8) ------> [[6, 3]]
we have 4 different sets of steps to test [2, 2, 4], [2, 4, 8], [2, 6, 12] and [2, 8, 16]

///so that we select primes p in the range (2, 30) that fulfill: p, p + 2, p + 2 and p + 4 all primes --- > only with prime 3 (1 prime)

p, p + 2, p + 4 and p + 8 all primes ----> only with prime 3 (1 prime)

p, p + 2, p + 6 and p + 12 all primes -----> passed by primes 5, 11, 17 (3 primes)

p, p + 2, p + 8 and p + 16 all primes -----> only with prime 3 (1 prime)

So h is 6 with 3 found primes (max amount of primes) ([6, 3])///

Case 2) For Python and Ruby

give_max_h(100, 10) -----> [[6, 4]] # with h = 6 we found the highest amount of primes (4) : 5, 11, 17, 41
For Javascript

giveMax_h(100, 10) -----> [[6, 4]]
Case 3) For Python and Ruby

give_max_h(1000, 100) -----> [[30, 13], [42, 13]] # we have two values of h that #procuded the highest amount of primes (13)
For Javascript

giveMax_h(1000, 100) -----> [[30, 13], [42, 13]]
///h = 30 produced the primes 11, 29, 41, 71, 107, 137, 197, 419, 431, 461, 617, 827, 881
h = 42 produced the primes 5, 17, 29, 107, 149, 197, 227, 269, 347, 419, 599, 617, 659
///
Happy coding!!

(Advise: You will need a fast prime generator. Do not use primality tests, otherwise the runtimes would exceed our allowed 6000 ms to complete tests)

(To investigate beyond this kata: Do we have a convergence for the value of h, no matter the values of n and hMax are?)
'''
import time
import numba as nb

global p
p = [2, 3, 5, 7, 11 , 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


# @nb.autojit
def genp(n):
    for np in range(101, n):
        isp = True
        for x in p:
            if np % x == 0:
                isp = False
                break
        if isp:
            p.append(np)
    return 1


def give_max_h(n, kMax):
#     genp(n + kMax * 2)
    p = sieve1(n + kMax * 2)
    if not p:
        return []
    result = []
    for x in range (2, kMax + 1, 2):
        count = 0
        tmp = 2 * x
        for z in p:
            if z < n and (z + 2 in p) and (z + x in p) and (z + tmp in p):
                count += 1
        if count > 0:
            result.append([x, count])
        
    result.sort(key=lambda x: x[1], reverse=True)
    if len(result) <= 1:
        return result
    result1 = []
    for x in result:
        if x[1] == result[0][1]:
            result1.append(x)  
    return result1


# @jit
def sieve1(n):
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


def sieve(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
#     print(n)
    correction = (n % 6 > 1)
    n = {0:n, 1:n - 1, 2:n + 4, 3:n + 3, 4:n + 2, 5:n + 1}[n % 6]
#     print(n)
    sieve = [True] * (n // 3)
    sieve[0] = False
    for i in range(int(n ** 0.5) // 3 + 1):
        if sieve[i]:
            k = 3 * i + 1 | 1
            sieve[      ((k * k) // 3)      ::2 * k] = [False] * ((n // 6 - (k * k) // 6 - 1) // k + 1)
            sieve[(k * k + 4 * k - 2 * k * (i & 1)) // 3::2 * k] = [False] * ((n // 6 - (k * k + 4 * k - 2 * k * (i & 1)) // 6 - 1) // k + 1)
    return [2, 3] + [3 * i + 1 | 1 for i in range(1, n // 3 - correction) if sieve[i]]


if __name__ == '__main__':
    beg = time.time()
    print(beg)
    genp(100000)
#     print(len(p))
#     genp(100000)

    mid = time.time()
    print(mid)
    fir = mid - beg
    print(mid - beg)
#     print(len(sieve1(100000)))
    sieve1(100000)
#     print(len(sieve(100000)))
#     print(len(p))
# #     print(p)
# 
#     print(give_max_h(1000, 100))
#     print(mid - beg)
#     print(time.time() - mid)
#     print(1 | 1)
    end = time.time()
    sec = end - mid
    print('new time:{}'.format(sec))
    print(fir / sec)
