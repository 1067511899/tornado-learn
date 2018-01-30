import tornado.httpserver   
import tornado.ioloop   
import tornado.web   
from tornado.options import define
import multiprocessing
'''
最直接的办法，用多进程调用。但是问题是每个实例只能绑定不同的端口，否则就会报错。
'''

define('port', default=8000, type=int)

class IndexHandler(tornado.web.RequestHandler):   
    def get(self):   

        quote = {'quote': (
                "I've always been more interested in "
                "the future than in the past."
            ),
            'author': 'Grace Hopper'
        }


        respon_json = tornado.escape.json_encode(quote)    
        self.write(respon_json)    

def startapp(port):
    print(port)
    app = tornado.web.Application(handlers=[(r"/", IndexHandler)])   
    http_server = tornado.httpserver.HTTPServer(app)   
    http_server.listen(port)   
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':   
    processes = [multiprocessing.Process(target=startapp,args=(i,)) for i in range(8881,8890)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()

