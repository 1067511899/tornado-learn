'''
Given an array, find the int that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

找出 数组里面 出现过基数次的数字
'''
def find_it(seq):
    dic = {}
    for x in seq:
        dic[x] = dic.get(x, 0) + 1
    keys = dic.keys()
    for y in keys:
        if dic[y] % 2:
            return y
    return None

# another result
def find_it1(seq):
    for i in seq:
        if seq.count(i) % 2 != 0:
            return i


if __name__ == '__main__':
    print(find_it([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]))
