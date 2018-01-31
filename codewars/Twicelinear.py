'''
Consider a sequence u where u is defined as follows:

The number u(0) = 1 is the first one in u.
For each x in u, then y = 2 * x + 1 and z = 3 * x + 1 must be in u too.
There are no other numbers in u.
Ex: u = [1, 3, 4, 7, 9, 10, 13, 15, 19, 21, 22, 27, ...]

1 gives 3 and 4, then 3 gives 7 and 10, 4 gives 9 and 13, then 7 gives 15 and 22 and so on...

#Task: Given parameter n the function dbl_linear (or dblLinear...) returns the element u(n) of the ordered (with <) sequence u.

#Example: dbl_linear(10) should return 22

#Note: Focus attention on efficiency
'''
# 441 471 the code has problem
def dbl_linear(n):
    if n == 1:
        return 1
    result = [1]
    for m in range(n):
        result.append(result[m] * 2 + 1)
        result.append(result[m] * 3 + 1)
    tmp = sorted(list(set(result)))
    for i, c in enumerate(tmp):
        print(i, c)
    return tmp[n]

if __name__ == '__main__':
    print(dbl_linear(471))
