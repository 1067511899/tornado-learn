'''
My friend John and I are members of the "Fat to Fit Club (FFC)". John is worried because each month a list with the weights of members is published and each month he is the last on the list which means he is the heaviest.

I am the one who establishes the list so I told him: "Don't worry any more, I will modify the order of the list". It was decided to attribute a "weight" to numbers. The weight of a number will be from now on the sum of its digits.

For example 99 will have "weight" 18, 100 will have "weight" 1 so in the list 100 will come before 99. Given a string with the weights of FFC members in normal order can you give this string ordered by "weights" of these numbers?

Example:
"56 65 74 100 99 68 86 180 90" ordered by numbers weights becomes: "100 180 90 56 65 74 68 86 99"

When two numbers have the same "weight", let us class them as if they were strings and not numbers: 100 is before 180 because its "weight" (1) is less than the one of 180 (9) and 180 is before 90 since, having the same "weight" (9) it comes before as a string.

All numbers in the list are positive numbers and the list can be empty.

Notes
it may happen that the input string have leading, trailing whitespaces and more than a unique whitespace between two consecutive numbers
Don't modify the input
For C: The result is freed.
1、数字按照它们的每个位数的和作为排序依据。
2、如果这些和相等，比如56和65，那么就把这两个数字当作字符串来进行比较，比如'56'<'65'
'''
from functools import cmp_to_key
def mycmp(a, b):
    aup = 0
    bup = 0
    aup = sum([int(i) for i in a])
    bup = sum([int[j] for j in b])
    
    if aup != bup:
        return aup - bup
    else:
        if a > b:
            return 1
        elif a < b:
            return -1
        else:
            return 0


def order_weight(strng):
    ls = strng.split()
    tmp = sorted(ls, key=cmp_to_key(mycmp))
    return ' '.join(tmp)



def weight_key(s):
    print(sum(int(c) for c in s), s)
    return (sum(int(c) for c in s), s)
def order_weight1(s):
    return ' '.join(sorted(s.split(' '), key=weight_key))


if __name__ == '__main__':
    print(order_weight1("103 123 4444 99 198 2000"))
    print(order_weight1("2000 10003 1234000 44444444 9999 11 11 22 123"))
