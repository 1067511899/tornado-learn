'''
Created on 2018年1月29日

@author: lenovo
'''
import unittest

class Test(unittest.TestCase):
    def assert_equals(self, fun, res, output=''):
        if self.assertEquals(fun, res, output) is not None:
            print(output)
        else:
            pass

if __name__ == '__main__':
    test = Test()
    test.assert_equals(12, 12,'sadfjklasfj')
