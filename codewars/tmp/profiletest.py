'''
Created on 2018年2月8日

@author: lenovo
'''
import cProfile

def fun():
    for i in range(1000000):
        a = i * i



if __name__ == '__main__':
    cProfile.run('fun()')
