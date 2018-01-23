'''
Created on 2018年1月19日

@author: lenovo
'''

class A():
    def __init__(self,invalue):
        self.invalue=invalue
        print('a init invalue:{}'.format(invalue))
        
        
    def a(self):
        print('A a')
        
class B(A):
    def __init__(self,invalue):
#         A.__init__(self)
#         super(B, self).__init__(invalue)
        A.__init__(self,invalue)
        self.invalue=invalue**2
        print('b invalue value: {}'.format(self.invalue))


class Rectangle():
    def __init__(self, w, h):
        print('Rectangle init')
        self.w = w
        self.h = h
    
    
    def area(self):
        return self.w * self.h
    
    
    def perimeter(self):
        return 2 * (self.w + self.h)




class Square(Rectangle):
    def __init__(self, s):
#         super().__init__(s, s)
        self.s = s

    def area(self):
        return self.s**2
#     def a(self):
#         raise NotImplementedError 
    
if __name__ == '__main__':
    tmp=Square(10)
    print(tmp.area())
    
    l=B(100)
    