'''
Task
You are given a string s. Every letter in s appears once.

Consider all strings formed by rearranging the letters in s. After ordering these strings in dictionary order, return the middle term. (If the sequence has a even length n, define its middle term to be the (n/2)th term.)

Example
For s = "abc", the result should be "bac".

The permutations in order are:
"abc", "acb", "bac", "bca", "cab", "cba"
So, The middle term is "bac".
Input/Output
[input] string s

unique letters (2 < length <= 26)

[output] a string

middle permutation.
'''
from itertools import product
# import time
def permutations(iterable, r=None):
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    for indices in product(range(n), repeat=r):
        if len(set(indices)) == r:
            yield tuple(pool[i] for i in indices)
            
            
def middle_permutation(string):
#     print('program begin:{}'.format(time.time()))
    tmp = permutations(string)
#     print('finish permutation:{}'.format(time.time()))
    tmp1 = dict.fromkeys(tmp)
#     print('finish remove duplicate by dict.formkeys:{}'.format(time.time()))
#     tmpuseless = set(tmp)
#     print('finish remove duplicate by set:{}'.format(time.time()))
    result = [''.join(x) for x in tmp1]
#     print('finish join:{}'.format(time.time()))
    result.sort()
#     print('finish sort:{}'.format(time.time()))
    le = len(result)
    if le % 2 == 0:
        return result[le // 2 - 1]
    else:
        return result[le // 2]
                 
# 其他人的解决办法,好吧,用permutation,基本上没可能准时完成任务了.
def middle_permutation1(string):
    s = "".join(sorted(string))
    mid = int(len(s) / 2) - 1
    if len(s) % 2 == 0:
        return s[mid] + (s[:mid] + s[mid + 1:])[::-1]
    else:
        return s[mid:mid + 2][::-1] + (s[:mid] + s[mid + 2:])[::-1]

if __name__ == '__main__':
    print(middle_permutation('abcdefghi'))
