import tornado.httpserver   
import tornado.ioloop   
import tornado.options   
import tornado.web   
from tornado.options import define, options   
import logging
# import ujson


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

if __name__ == '__main__':   
    tornado.options.parse_command_line()   
    logging.getLogger('tornado.access').disabled = True

    app = tornado.web.Application(handlers=[(r"/", IndexHandler)])   
    http_server = tornado.httpserver.HTTPServer(app)   
    http_server.listen(options.port)   
    tornado.ioloop.IOLoop.instance().start()