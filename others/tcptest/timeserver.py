from socket import *
from time import ctime

HOST = ''
PORT = 8888
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print('waiting')
    tcpCliSock, addr = tcpSerSock.accept()
    print('connect from ', addr)
    while True:
        data = tcpCliSock.recv(BUFSIZE)
        if not data:
            break
        tcpCliSock.send(('[%s] %s' % (ctime(), data)).encode())
    
    tcpCliSock.close()
tcpSerSock.close()
