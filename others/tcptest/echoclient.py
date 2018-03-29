import socket
import time

HOST = '192.168.1.157'
PORT = 7


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
#     count = 10
#     while count > 0:
#         data = str(time.time())
#         s.sendall(data.encode())
#         data = s.recv(1024)
#         if not data:
#             break
#         print('{}'.format(data))
#         time.sleep(2)
#         count -= 1

#     s.sendall(data.encode())
#     data = s.recv(1024)

    s.close()


if __name__ == '__main__':
    main()
