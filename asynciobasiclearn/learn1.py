import asyncio

def hello_world(loop):
    print('Hello World')
    print(loop.is_running())

    loop.stop()

loop = asyncio.get_event_loop()

# Schedule a call to hello_world()
loop.call_soon(hello_world, loop)

# Blocking call interrupted by loop.stop()
loop.run_forever()
print(loop.is_running())
print(loop.is_closed())
loop.close()