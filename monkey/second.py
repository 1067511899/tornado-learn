'''
一个monkey patch的例子，另外，pydev在import的时候总是报错，但不影响代码使用。
'''

from first import Foo


def monkeydetail(self):
    print('name:  {}\nage:  {}'.format(self.name, self.age))


Foo.detail = monkeydetail

xiaoli = Foo('xiaoli', 20)
xiaoli.detail()
