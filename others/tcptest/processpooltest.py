'''
Created on 2018年4月3日

@author: lenovo
'''
from concurrent.futures.process import ProcessPoolExecutor
import time


def longtime():
    print('longtime')
#     time.sleep(1000)

    
def shorttime():
    print('shorttime')
    time.sleep(2000)


if __name__ == '__main__':
    executor = ProcessPoolExecutor()
#     p1 = Process(target=tcp_task, args=(HOST, PORT,))
#     p1.start()

    a = executor.submit(longtime)
    print(a.result)
    b = executor.submit(shorttime)
    print(b.result)
    print(b.running())
#     print(b.cancel())
    print(a.running())

