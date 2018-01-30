'''
Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.

For example:

 persistence(39) => 3  # Because 3*9 = 27, 2*7 = 14, 1*4=4
                       # and 4 has only one digit.

 persistence(999) => 4 # Because 9*9*9 = 729, 7*2*9 = 126,
                       # 1*2*6 = 12, and finally 1*2 = 2.

 persistence(4) => 0   # Because 4 is already a one-digit number.
 persistence(39) # returns 3, because 3*9=27, 2*7=14, 1*4=4
                 # and 4 has only one digit

 persistence(999) # returns 4, because 9*9*9=729, 7*2*9=126,
                  # 1*2*6=12, and finally 1*2=2

 persistence(4) # returns 0, because 4 is already a one-digit number
'''
from _functools import reduce
import time
def persistence(n):
    count=0
    while(len(str(n))>1):
        count+=1
        tmp=str(n)
        n=1
        for x in tmp:
            n=n*int(x)
    return count

import operator
def persistence1(n):
    i = 0
    while n>=10:
        n=reduce(operator.mul,[int(x) for x in str(n)],1)
        i+=1
    return i


if __name__=='__main__':
    begin=time.time()
    persistence(9888986647477777777777777777777)
    end1=time.time()
    persistence1(9888986647477777777777777777777)
    end2=time.time()
    print(end1-begin)
    print(end2-end1)