import socket
import sys

HOST, PORT = "127.0.0.1", 8888
data = 'tcp test client'

# Create a socket (SOCK_STREAM means a TCP socket)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    sock.sendall(bytes(data + "\n", "utf-8"))
#     sock.sendall(data)
    received = sock.recv(1024)
    print(type(received))
    # Receive data from the server and shut down
    received = str(received, "utf-8")

print("Sent:     {}".format(data))
print("Received: {}".format(received))
