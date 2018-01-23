'''
Created on 2018年1月22日

@author: lenovo
'''
'''
*args：输入数据长度不确定，通过*args将任意长度的参数传递给函数，系统自动将任意长度参数用list表示

**kargs：输入数据长度不确定，系统自动将任意长度参数用dict（字典）表示


'''
def getargs(*arg):
    print(arg)
    

def getkargs(**kargs):
    print(kargs)
if __name__ == '__main__':
    getargs(1,2,3)
    getkargs(a=10,b=12)