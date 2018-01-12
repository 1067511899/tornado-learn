'''
Created on 2018年1月11日

@author: lenovo
'''
import time

print(time.time())
a = frozenset(range(1000000000))
print(time.time())
b = frozenset(range(500000000, 2000000000))

print(len(a & b))

print(time.time())