'''
Divisors of 42 are : 1, 2, 3, 6, 7, 14, 21, 42. These divisors squared are: 1, 4, 9, 36, 49, 196, 441, 1764. The sum of the squared divisors is 2500 which is 50 * 50, a square!

Given two integers m, n (1 <= m <= n) we want to find all integers between m and n whose sum of squared divisors is itself a square. 42 is such a number.

The result will be an array of arrays or of tuples (in C an array of Pair) or a string, each subarray having two elements, first the number whose squared divisors is a square and then the sum of the squared divisors.

#Examples:

list_squared(1, 250) --> [[1, 1], [42, 2500], [246, 84100]]
list_squared(42, 250) --> [[42, 2500], [246, 84100]]
The form of the examples may change according to the language, see Example Tests: for more details.
'''
import time
def list_squared(m, n):
    result = []
    for x in range(m, n + 1):
        sumx = 0
        sqrtx = int(x ** 0.5) + 1
        for i in range(1, sqrtx):
            if x % i == 0:
                tmp = x // i
                if tmp != i:
                    sumx = sumx + i ** 2 + (tmp) ** 2
                else:
                    sumx += tmp ** 2
        
        if int(sumx ** 0.5) ** 2 == sumx:
            result.append([x, sumx])
    return result


if __name__ == '__main__':
    beg = time.time()
    print(list_squared(1, 251110))
    print(time.time() - beg)
