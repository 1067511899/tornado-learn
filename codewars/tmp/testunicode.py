'''
Created on 2018年2月2日

@author: lenovo
'''



if __name__ == '__main__':
    tmp = [hex(ord(x)) for x in 'well']
    print(''.join(tmp).replace('0x', ''))
    x = 1100
    y = 200
    tmp1 = x if x < y else y
    print(tmp1)
