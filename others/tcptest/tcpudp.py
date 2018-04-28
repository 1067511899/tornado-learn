import socketserver
from multiprocessing import Process, Pool
import time
from concurrent.futures.thread import ThreadPoolExecutor
from concurrent.futures.process import ProcessPoolExecutor


class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        print('tcp handler')
        self.data = self.request.recv(1024).strip()
        print("{} tcp handler wrote:".format(self.client_address[0]))
        print(self.data)
        # just send back the same data, but upper-cased
        self.request.sendall(self.data.upper())


class MyUDPHandler(socketserver.BaseRequestHandler):
    """
    This class works similar to the TCP handler class, except that
    self.request consists of a pair of data and client socket, and since
    there is no connection the client address must be given explicitly
    when sending data back via sendto().
    """

    def handle(self):
        data = self.request[0].strip()
        print('udp handler')
        socket = self.request[1]
        print("{} udphandler wrote:".format(self.client_address[0]))
        print(data)
        socket.sendto(data.lower(), self.client_address)
        
        
def tcp_task(host, port):
    print(host, port)
    server = socketserver.TCPServer((host, port), MyTCPHandler)
    try:
        print('start tcp server')
        server.serve_forever()
    except Exception as e:
        print(e)


def udp_task(host, port):
    print(host, port)
    server = socketserver.UDPServer((host, port), MyUDPHandler)
    try:
        print('start udp server')
        server.serve_forever()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    HOST, PORT = "127.0.0.1", 8888
    executor = ThreadPoolExecutor()
#     p1 = Process(target=tcp_task, args=(HOST, PORT,))
#     p1.start()

    a = executor.submit(tcp_task, HOST, PORT)

    b = executor.submit(udp_task, HOST, PORT)

# 
#     p = Process(target=udp_task, args=(HOST, PORT,))
# 
#     p.start()
#     p.join()

#     with socketserver.UDPServer((HOST, PORT), MyUDPHandler) as server:
#         print('start udp server')
#         server.serve_forever()

#     while True:
#         time.sleep(1)

