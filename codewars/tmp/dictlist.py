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
