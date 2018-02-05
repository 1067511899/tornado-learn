'''
The prime numbers are not regularly spaced. For example from 2 to 3 the gap is 1. From 3 to 5 the gap is 2. From 7 to 11 it is 4. Between 2 and 50 we have the following pairs of 2-gaps primes: 3-5, 5-7, 11-13, 17-19, 29-31, 41-43

A prime gap of length n is a run of n-1 consecutive composite numbers between two successive primes (see: http://mathworld.wolfram.com/PrimeGaps.html).

We will write a function gap with parameters:

g (integer >= 2) which indicates the gap we are looking for

m (integer > 2) which gives the start of the search (m inclusive)

n (integer >= m) which gives the end of the search (n inclusive)

In the example above gap(2, 3, 50) will return [3, 5] or (3, 5) or {3, 5} which is the first pair between 3 and 50 with a 2-gap.

So this function should return the first pair of two prime numbers spaced with a gap of g between the limits m, n if these numbers exist otherwise nil or null or None or Nothing (depending on the language).

In C++ return in such a case {0, 0}. In F# return [||]. In Kotlin return []

#Examples: gap(2, 5, 7) --> [5, 7] or (5, 7) or {5, 7}

gap(2, 5, 5) --> nil. In C++ {0, 0}. In F# [||]. In Kotlin return[]`

gap(4, 130, 200) --> [163, 167] or (163, 167) or {163, 167}

([193, 197] is also such a 4-gap primes between 130 and 200 but it's not the first pair)

gap(6,100,110) --> nil or {0, 0} : between 100 and 110 we have 101, 103, 107, 109 but 101-107is not a 6-gap because there is 103in between and 103-109is not a 6-gap because there is 107in between.

Note for Go
For Go: nil slice is expected when there are no gap between m and n. Example: gap(11,30000,100000) --> nil

#Ref https://en.wikipedia.org/wiki/Prime_gap
'''

def gap(g, m, n):
    firstp = None
    for x in range(m, n + 1):
        big = int((n + 1) ** 0.5) + 1
        ispri = True
        for y in range(2, big):
            if x % y == 0:
                ispri = False
                break
        if ispri:
            firstp = x
            break
    if firstp:
        print(firstp)
        for x in range(firstp + 1, n + 1):
            big = int(n ** 0.5) + 1
            ispri = True
            for y in range(2, big):
                if x % y == 0:
                    ispri = False
                    break
            if ispri:
                if x - firstp == g:
                    return [firstp, x]
                else:
                    firstp = x
    return None

# 这道题我显然太功利了，还是应该抽取求质数的代码作为 函数。另外，整个逻辑也是不清楚。
# 当然，如果我求出所有质数，然后再找头两个，那么性能上会很差，过不了测试。

def gap1(g, m, n):
    previous_prime = n
    for i in range(m, n + 1):
        if is_prime(i):
            if i - previous_prime == g: 
                return [previous_prime, i]
            previous_prime = i
    return None
            
    
def is_prime(n):
    for i in range(2, int(n ** .5 + 1)):
        if n % i == 0:
            return False
    return True
            

if __name__ == '__main__':
    print(gap(8, 300, 400))
