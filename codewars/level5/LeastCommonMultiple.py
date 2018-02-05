'''
Write a function that calculates the least common multiple of its arguments; each argument is assumed to be a non-negative integer. In the case that there are no arguments (or the provided array in compiled languages is empty), return 1.
'''
from _functools import reduce
def gcm(a, b):  
    if a > b:
        a, b = b, a
    while (b % a != 0):
        a, b = b % a, a
    return a
  
def lcm1(a, b):  
    return a * b // gcm(a, b)  

def lcm(*args):
    le = len(args)
    if le <= 1:
        return args[0]
    if 0 in args:
        return 0
    result = lcm1(args[0], args[1])
    for x in range(2, le):
        result = lcm1(result, args[x])
    return result


from fractions import gcd
# 竟然还有这种操作，竟然不用自己写代码来求最大公约数
def lcm2(*args):
    return reduce(lambda x, y: x * y / gcd(x, y), args)


if __name__ == '__main__':
    print(lcm(2, 3, 4))
#     print(gcm(96, 121132))
