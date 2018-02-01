'''
Given two numbers: 'left' and 'right' (1 <= 'left' <= 'right' <= 200000000000000) return sum of all '1' occurencies in binary representations of numbers between 'left' and 'right' (including both)

Example:
countOnes 4 7 should return 8, because:
4(dec) = 100(bin), which adds 1 to the result.
5(dec) = 101(bin), which adds 2 to the result.
6(dec) = 110(bin), which adds 2 to the result.
7(dec) = 111(bin), which adds 3 to the result.
So finally result equals 8.
WARNING: Segment may contain billion elements, to pass this kata, your solution cannot iterate through all numbers in the segment!
完全不会

'''
def countOnes(left, right):
    def f(n):
        c = 0
        a = list(reversed(list(bin(n))))
        for i, d in enumerate(a):
            if d == '1':
                c += 1 + 2 ** i * i / 2 + 2 ** i * a[i + 1:].count('1')
        return c
    return f(right) - f(left - 1)


if __name__ == '__main__':
    pass
