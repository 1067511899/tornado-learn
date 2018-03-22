from time import sleep, time, localtime, strftime
import urllib.request
import logging

fhand = logging.FileHandler('new20180320.log', mode='a', encoding='GBK')

logging.basicConfig(level=logging.DEBUG,  # 控制台打印的日志级别
                    handlers=[fhand],
                    format=
                    '%(asctime)s  - %(levelname)s: %(message)s'
                    # 日志格式
                    )


def check1(url):
    try:
        file = urllib.request.urlopen(url)
#         logging.info(url)
#         print(url, file.getcode())
    except Exception as e:
        print(strftime("%Y-%m-%d %H:%M:%S", localtime(time())))
#         print(file.body)
        logging.info(url)
        logging.info(e)
        print(url, e)

    
if __name__ == '__main__':
    while True:
        print(strftime("%Y-%m-%d %H:%M:%S", localtime(time())))
        logging.debug(strftime("%Y-%m-%d %H:%M:%S", localtime(time())))
        check1('http://pms.yhsoft.com/') 
        check1('http://www.baidu.com')
        check1('http://www.gtax.cn')
#         check1('http://192.168.1.157:8888')
#         check1('https://oa.yhsoft.com')
        sleep(10)
