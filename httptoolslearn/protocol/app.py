"""
这是实现的一个最基本的基于httptools和asyncio的web服务器。
总算把主要的关系理顺了。
"""


import httptools
import asyncio
from httptools.parser.errors import HttpParserError

RESPONSE1_HEAD = b'''HTTP/1.1 200 OK
Date: Mon, 23 May 2005 22:38:34 GMT
Server: Apache/1.3.3.7
        (Unix) (Red-Hat/Linux)
Last-Modified: Wed, 08 Jan 2003 23:11:55 GMT
ETag: "3f80f-1b6-3e1cb03b"
Content-Type: text/html;
  charset=UTF-8
Content-Length: 130
Accept-Ranges: bytes
Connection: close

'''

RESPONSE1_BODY = b'''
<html>
<head>
  <title>An Example Page</title>
</head>
<body>
  Hello World, this is a very simple HTML document.
</body>
</html>'''


res = RESPONSE1_HEAD + RESPONSE1_BODY

class BaseHttpServer(asyncio.Protocol):

    def __init__(self):
        self.parser = httptools.HttpRequestParser(self)
        self.transport = None

    def connection_made(self, transport):
        print('start', transport)
        self.transport = transport

    def data_received(self, data):
        print('in data_received')
        print(data)
        try:
            self.parser.feed_data(data)
        except HttpParserError:
            message = 'Bad Request'
            print(message)

    def connection_lost(self, exc):
        print('stop', exc)

    def on_header(self, name, value):
        print(name, value)

    def on_headers_complete(self):
        self.transport.write(res)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    coro = loop.create_server(BaseHttpServer, '127.0.0.1', 8888)
    server = loop.run_until_complete(coro)
    loop.run_forever()




