import httptools
import asyncio
from httptools.parser.errors import HttpParserError


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
    t.data_received(CHUNKED_REQUEST1_1)
