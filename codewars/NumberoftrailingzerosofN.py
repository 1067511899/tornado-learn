'''

# 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720 --> 1 trailing zero

zeros(12) = 2
# 12! = 479001600 --> 2 trailing zeros
Hint: You're not meant to calculate the factorial. Find another way to find the number of zeros.
'''

# 没搞定，答案是错的
def zeros(n):
    count5 = 0
    count10 = 0
    countodd = 0
    zero = 0
    for x in range(2, n + 1):
        tmp = str(x).lstrip('0')
        if int(tmp) % 2 == 0 :
            countodd += 1
        if int(tmp) % 5 == 0:
            count5 += 1
        count10 += len(str(x)) - len(tmp)
    if count5 > countodd:
        zero = countodd
    else:
        zero = count5
    zero += count10
    
    return zero


if __name__ == '__main__':
    print(zeros(6))
