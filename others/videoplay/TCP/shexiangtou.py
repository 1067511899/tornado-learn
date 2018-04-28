import cv2
import time
from PIL import Image
import numpy
import socket
from io import StringIO
from io import BytesIO
from PIL import ImageGrab
import struct

IP = "localhost"
PORT = 9999
address = (IP, PORT)
PIC = 101
VOIEC = 102


def to_package(byte, cmd, ver=1):
    '''
    将每一帧的图片流的二进制数据进行分包
    :param byte: 二进制文件
    :param cmd:命令
    :return: 
    '''
    head = [ver, len(byte), cmd]
    headPack = struct.pack("!3I", *head)
    senddata = headPack + byte
    return senddata


def pic_to_array(pic):
    '''
    将图片转化为numpy数组
    :param pic: 
    :return: 
    '''
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


def tcp_camera(process=None):
    '''
    通过tcp协议传输每一帧图片
    :param process: 
    :return: 
    '''
    cam = cv2.VideoCapture(0)  # 打开摄像头
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 构建tcp套接字
    sock.connect(address)
    while cam.isOpened():
        ret, frame = cam.read()  # 读取摄像头信息
        if ret == True:
            cv2.imshow("transmitting", frame)  # 显示
            if process:
                '''
                视频处理模块
                '''
                frame = process(frame)
            jepg = array_pic_to_stream(frame)  # 将图片转化为二进制流
            print(len(jepg))
            package = to_package(jepg, 101)  # 封包
            try:
                sock.send(package)
            except:
                cont = input("远程连接断开,是否重新连接? Y:重新连接 N:退出程序")
                if(cont.lower() == "n"):
                    return
                if(cont.lower() == "y"):
                    cam.release()
                    cv2.destroyAllWindows()
                    sock.close()
                    tcp_camera()
            if (cv2.waitKey(1) & 0xFF) == ord('q'):
                break
            else:
                continue
    # 关闭自愿
    cam.release()
    cv2.destroyAllWindows()
    sock.close()


def tcp_screen(process=None):
    '''
        将本地屏幕发送到客户端
        :param process: 
        :param fps: 
        :return: 
        '''
    # 构建套接字
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(address)
    while True:
        img = ImageGrab.grab()
        img = pic_to_array(img)
        if process:
            frame = process(img)
        # cv2.imshow("screen",img)
        jepg = array_pic_to_stream(img)
        jepg = to_package(jepg, 101)
        print(len(jepg))
        try:
            sock.send(jepg)
        except:
            cont = input("远程连接失败,是否重新连接? Y:重新连接 N:退出程序")
            if (cont.lower() == "n"):
                print("程序退出......")
                return
            if (cont.lower() == "y"):
                cv2.destroyAllWindows()
                sock.close()
                tcp_screen()
        # cv2.imshow("cra", img)
        cv2.waitKey(1)
        if (cv2.waitKey(1) & 0xFF) == ord('q'):
            break
        else:
            continue
    sock.close()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    tcp_camera()
