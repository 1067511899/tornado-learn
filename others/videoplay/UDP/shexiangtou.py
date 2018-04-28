import cv2
import time
from PIL import Image
import numpy
import socket
from io import StringIO
from io import BytesIO
from PIL import ImageGrab


IP = "127.0.0.1"
PORT = 9999
address = (IP,PORT)

def pic_to_array(pic):
    stram = BytesIO()
    pic.save(stram, format="JPEG")
    array_pic = numpy.array(Image.open(stram))
    stram.close()
    return array_pic

def array_pic_to_stream(pic):
    '''
    将数组图片转化为byte
    :param pic: 
    :return: 
    '''
    stream = BytesIO()
    pic = Image.fromarray(pic)
    pic.save(stream, format="JPEG")
    jepg = stream.getvalue()
    stream.close()
    return jepg

def carema(process=None):
    # 构建套接字
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    cam = cv2.VideoCapture(0)
    while (cam.isOpened()):
        ret,frame = cam.read()
        if ret == True:
            cv2.imshow("transmitting",frame)
            if process:
                frame = process(frame)
            jepg = array_pic_to_stream(frame)
            print(len(jepg))
            sock.sendto(jepg,address)
            cv2.waitKey(1)
        if (cv2.waitKey(1) & 0xFF) == ord('q'):
            break
        else:
            continue
    cam.release()
    cv2.destroyAllWindows()
    sock.close()
def screen(process=None,fps=0.01):
    # 构建套接字
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        img = ImageGrab.grab()

        out = img.resize((612,480))

        img = pic_to_array(out)

        if process:
            frame = process(img)
        #cv2.imshow("screen",img)
        jepg = array_pic_to_stream(img)
        print(len(jepg))
        sock.sendto(jepg,address)
        cv2.imshow("cra",img)
        cv2.waitKey(1)
        if (cv2.waitKey(1) & 0xFF) == ord('q'):
            break
        else:
            continue
    sock.close()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    carema()
