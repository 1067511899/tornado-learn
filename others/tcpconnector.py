import argparse, socket
from time import sleep, time, localtime, strftime
import time
import logging

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


def client(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    print('Client has been assigned socket name', sock.getsockname())
    sock.sendall(b'hi')
    reply = recvall(sock, 16)
    print('reply', repr(reply))
    sock.close()

    
if __name__ == '__main__':
    while True:
        
        print(strftime("%Y-%m-%d %H:%M:%S", localtime(time.time())))
        try:
            client('183.63.81.42', 443)
#             client('192.168.1.251', 80)
        except Exception as e:
            print(e)
            logging.info(e)
        
        time.sleep(10)
