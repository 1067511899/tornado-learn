import asyncio
import time
 
now = lambda : time.time()
 
async def do_some_work(x):
    print('Waiting: ', x)
    return x

def callback(future):
    print('Callback: ', future.result())

start = now()
 
coroutine = do_some_work(2)
loop = asyncio.get_event_loop()
print(asyncio.get_event_loop_policy())
# task = asyncio.ensure_future(coroutine)
task = loop.create_task(coroutine)
print(task)
#可以通过增加 完成之后的callback，对返回的数据进行处理
task.add_done_callback(callback)
loop.run_until_complete(task)
print(task)
#也可以直接处理
print(task.result())
print('TIME: ', now() - start)