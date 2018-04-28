'''
Created on 2018年4月24日

@author: lenovo
'''


def funtest(arg):
    print(arg)
    

def returnfun():
    return funtest


if __name__ == '__main__':
    returnfun()('test')
