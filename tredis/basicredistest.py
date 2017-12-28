'''
Created on 2017年12月28日

@author: lenovo
'''
import redis

r = redis.StrictRedis(host='192.168.2.55', port=6379, db=0)
print(r.set('foo', 'bar'))

print(r.get('foo'))