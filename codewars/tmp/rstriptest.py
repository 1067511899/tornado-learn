'''
Created on 2018年1月30日

@author: lenovo
'''
def increment_string(strng):
    head = strng.rstrip('0123456789')
    tail = strng[len(head):]
    print(head, tail)

if __name__ == '__main__':
    increment_string('foo6677bar00999')
