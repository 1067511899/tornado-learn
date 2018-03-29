import socketserver
from multiprocessing import Process, Pool
import time


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
        
        
def tcp_task():
    server = socketserver.TCPServer(('0.0.0.0', 8888), MyTCPHandler)
    try:
        print('start tcp server')
        server.serve_forever()
    except Exception as e:
        print(e)


def udp_task():
    server = socketserver.UDPServer(('0.0.0.0', 8888), MyUDPHandler)
    try:
        print('start udp server')
        server.serve_forever()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    HOST, PORT = "localhost", 8888

    p1 = Process(target=tcp_task)
    p1.start()
# #     p1.join()
#     print('main')
#     p = Process(target=udp_task)
#     p.start()
#     p.join()
#     p = Pool(4)
#     for i in range(4):
#         p.apply_async(httpd_task)
#     p.close()
#     p.join()
    # Create the server, binding to localhost on port 9999
    with socketserver.UDPServer((HOST, PORT), MyUDPHandler) as server:
        print('start udp server')
        server.serve_forever()

