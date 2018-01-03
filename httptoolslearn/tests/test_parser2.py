import httptools

import unittest
from unittest import mock
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



# - on_message_begin()
# - on_header(name: bytes, value: bytes)
# - on_headers_complete()
# - on_body(body: bytes)
# - on_message_complete()
# - on_chunk_header()
# - on_chunk_complete()

#NI:not implemention
#根据httptools初始化参数：def __init__(self, protocol):，需要传一个协议过去。
#反正我知道的做法之一，就是写在协议的实现里面。然后调用各种on的回调函数。
#如果要拿这个替换tornado本身的parser，基本上要重写http1connection.py了。

class HttpProtocol(asyncio.Protocol):
    def __init__(self):
        self.parser = None
        self.url = None
        self.headers = None
        
    def data_received(self, data):
        
        if self.parser is None:
            self.headers = []
            self.parser = httptools.HttpResponseParser(self)


        try:
            self.parser.feed_data(data)
        except HttpParserError:
            message = 'Bad Request'
            print(message)
            
    def on_message_begin(self):
        print('NI on_message_begin')
        
    
    def on_header(self,name,value):
        print(name,value)
    

    def on_headers_complete(self):
        print('NI on_headers_complete')
        
    
    def on_body(self,body):
        print(body)

    
    def on_message_complete(self):
        print('NI on_message_complete')
    

    def on_chunk_header(self):
        print('NI on_chunk_header')
        
    
    def on_chunk_complete(self):
        print('NI on_chunk_complete')
 

if __name__ == '__main__':
    t=HttpProtocol()
    t.data_received(RESPONSE1_HEAD+RESPONSE1_BODY)
    
    