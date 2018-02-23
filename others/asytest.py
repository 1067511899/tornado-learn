import asyncio


async def get_chat_id(name):
    await asyncio.sleep(3)
    return "chat-%s" % name


def main():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(get_chat_id("django"))
    print(result)


if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(get_chat_id("django"))
    print(result)
    print('sync')
