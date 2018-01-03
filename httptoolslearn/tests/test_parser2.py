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


CHUNKED_REQUEST1_1 = b'''POST /test.php?a=b+c HTTP/1.2
User-Agent: Fooo
Host: bar
Transfer-Encoding: chunked

5\r\nhello\r\n6\r\n world\r\n'''

CHUNKED_REQUEST1_2 = b'''0\r\nVary: *\r\nUser-Agent: spam\r\n\r\n'''

CHUNKED_REQUEST1_3 = b'''POST /test.php?a=b+c HTTP/1.2
User-Agent: Fooo
Host: bar
Transfer-Encoding: chunked

b\r\n+\xce\xcfM\xb5MI,I\x04\x00\r\n0\r\n\r\n'''


UPGRADE_REQUEST1 = b'''GET /demo HTTP/1.1
Host: example.com
Connection: Upgrade
Sec-WebSocket-Key2: 12998 5 Y3 1  .P00
Sec-WebSocket-Protocol: sample
Upgrade: WebSocket
Sec-WebSocket-Key1: 4 @1  46546xW%0l 1 5
Origin: http://example.com

Hot diggity dogg'''

UPGRADE_RESPONSE1 = b'''HTTP/1.1 101 Switching Protocols
UPGRADE: websocket
SEC-WEBSOCKET-ACCEPT: rVg+XakFNFOxk3ZH0lzrZBmg0aU=
TRANSFER-ENCODING: chunked
CONNECTION: upgrade
DATE: Sat, 07 May 2016 23:44:32 GMT
SERVER: Python/3.4 aiohttp/1.0.3

data'''.replace(b'\n', b'\r\n')


class HttpProtocol(asyncio.Protocol):
    def __init__(self):
        self.parser = None
        self.url = None
        self.headers = None
        
    def data_received(self, data):
        
        if self.parser is None:
            self.headers = []
            self.parser = httptools.HttpRequestParser(self)


        try:
            self.parser.feed_data(data)
        except HttpParserError:
            message = 'Bad Request'
            print(message)

    def on_headers_complete(self):
        print('NI')
        
    
#     def on_header(self, name, value):
#         self._header_fragment += name
#         print('NI1')

#         if value is not None:
# #             if self._header_fragment == b'Content-Length' \
# #                     and int(value) > self.request_max_size:
# #                 exception = PayloadTooLarge('Payload Too Large')
# #                 self.write_error(exception)
#             try:
#                 value = value.decode()
#             except UnicodeDecodeError:
#                 value = value.decode('latin_1')
#             self.headers.append(
#                     (self._header_fragment.decode().casefold(), value))
# 
#             self._header_fragment = b''
        
        
    

class TestRequestParser():

    def test_parser_request_chunked_1(self):
        m = mock.Mock()

        p = httptools.HttpRequestParser(m)

        p.feed_data(UPGRADE_REQUEST1)

        print(p.get_method())
 

if __name__ == '__main__':
    t=HttpProtocol()
    t.data_received(CHUNKED_REQUEST1_1)
    
    