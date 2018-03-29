import argparse, socket
from time import sleep, time, localtime, strftime
import time
import logging
import sys
import trace

fhand = logging.FileHandler('new20180321.log', mode='a', encoding='GBK')

logging.basicConfig(level=logging.DEBUG,  # 控制台打印的日志级别
                    handlers=[fhand],
                    format=
                    '%(asctime)s  - %(levelname)s: %(message)s'
                    # 日志格式
                    )


def recvall(sock, length):
    data = b''
    while len(data) < length:
        more = sock.recv(length - len(data))
        if not more:
            raise EOFError('was expecting %d bytes but only received %d bytes before the socket closed'
                           % (length, len(data)))
        data += more
    return data


header = '''
GET / HTTP/1.1\r\n
    Host: 192.168.1.157:8000\r\n
    Connection: keep-alive\r\n
    Upgrade-Insecure-Requests: 1\r\n
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36\r\n
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8\r\n
    DNT: 1\r\n
    Accept-Encoding: gzip, deflate\r\n
    Accept-Language: zh-CN,zh;q=0.9\r\n
    If-None-Match: "15e84b11ce57dec1b9483884f4e5587e71d5c201"\r\n
    \r\n
'''
CRLF = "\r\n\r\n"


def client(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    print('Client has been assigned socket name', sock.getsockname())
    sock.send((header).encode())
    print(header.encode())
    reply = recvall(sock, 160)
    print('reply', repr(reply))
    sock.close()


def main():
    print(strftime("%Y-%m-%d %H:%M:%S", localtime(time.time())))
    try:
#         client('183.63.81.42', 80)
        client('192.168.1.157', 8000)
    except Exception as e:
        print(e)
        logging.info(e)
        
        
if __name__ == '__main__':
    print(strftime("%Y-%m-%d %H:%M:%S", localtime(time.time())))
    client('https://www.baidu.com', 443)

