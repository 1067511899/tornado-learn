'''
Created on 2018年5月24日

@author: lenovo
'''
import math


def dd(lin=[]):
    eve = sum(lin) / len(lin)
    print(eve)
    delt = math.sqrt(sum([(x - eve) ** 2 for x in lin]) / len(lin))
    print(delt)
    
    
if __name__ == '__main__':
    test = [x for x in range(100)]
    test = [0, 5, 9, 14]
    test1 = [5, 6, 8, 9]
    dd(test)
    dd(test1)
