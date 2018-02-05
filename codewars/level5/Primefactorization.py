'''
The prime factorization of a positive integer is a list of the integer's prime factors, together with their multiplicities; the process of determining these factors is called integer factorization. The fundamental theorem of arithmetic says that every positive integer has a single unique prime factorization.

The prime factorization of 24, for instance, is (2^3) * (3^1).

Write a class called PrimeFactorizer (inheriting directly from object) whose constructor accepts exactly 1 int and has a property factor containing a dictionary where the keys are prime numbers and the values are the multiplicities.

PrimeFactorizer(24).factor #should return { 2: 3, 3: 1 }
'''
from collections import Counter
def is_prime(n):
    for i in range(2, int(n ** .5 + 1)):
        if n % i == 0:
            return False
    return True


class PrimeFactorizer:
    def __init__(self, n):
        self.n = n
        self.factor = []
        self.__ca__(self.n)
        self.factor = dict(Counter(self.factor))
    
    
    def __ca__(self, n):
        i = 2
        tmp = int(n ** .5 + 1) + 1
        print(tmp)
        while i < tmp:
            if n % i == 0:
                self.factor.append(i)
                n = n // i
            else:
                i += 1
        if n != 1:
            self.factor.append(n)
        
        if not self.factor:
            self.factor = [self.n]

# 好吧，啥时候我能写出这么优雅的代码？
class PrimeFactorizer1:

    def __init__(self, num):
        self.factor = {}
        for i in range(2, num + 1):
            if (num < i):
                break
            while(num % i == 0):
                num /= i
                self.factor[i] = self.factor.get(i, 0) + 1

if __name__ == '__main__':
    print(PrimeFactorizer(10967535067).factor)
