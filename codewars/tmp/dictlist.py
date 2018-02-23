'''
Created on 2018年1月31日

@author: lenovo
'''
import collections



if __name__ == '__main__':
    dic = collections.OrderedDict()
    a = [12, 15]
    b = [11, 22, 33]
    c = {}
    c[1] = a
    c[1] = b
    c[2] = c.get(2, [])
    c[2].append('dd')
    c.get(0, []).append('try')
    
    
    tmp = b[0]
    tmp = 'a'
    print(c)
    print(sum({20, 10, -80, 10, 10, 15, 35}))
    website = ['codewars'] * 10
    print(website)
    print('gold' in ['gold', 1, 2])
    print(sum([1, 2, 3]))
    print('8 j 8   mBliB8g  imjB8B8  jl  B'.replace(' ', ''))
    tmp = []
    for x in range(5, 0, -1):
        tmp.append(x)
    tmp.reverse()
    print(list(range(5, 0, -1)))
    a = ["a", "a", "b", "b"]
    b = ["a", "c", "b", "d"]
    print('helFlo'.upper())
    print(not(15 % 5))
    print(not(-12 % 2) and not(-12 % -5))
    print(-12 % 2 and -12 % -5)
    print(-12 % -5)
    print('eloquent'[1:-1])
    print(42 ** 3 <= 105462)
    print(sorted(['Algebra', 'history', 'Geometry', 'english']))
    print("{%.2f}" % (123 / 1.15))
