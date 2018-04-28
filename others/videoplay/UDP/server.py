import socket
import cv2
import numpy
from io import BytesIO
from PIL import Image

IP = ""
PORT = 9999
address = (IP,PORT)

def receive(process=None):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(address)
    while True:
        img,addr= sock.recvfrom(1024*1024)
        buf = BytesIO(img)
        img = numpy.array(Image.open(buf))
        a = Image.open(buf)
        #a.show()
        cv2.imshow("receive",img)
        buf.close()
        if (cv2.waitKey(1) & 0xFF) == ord('q'):
            break
        else:
            continue
    cv2.destroyAllWindows()
    sock.close()


if __name__=="__main__":
    receive()