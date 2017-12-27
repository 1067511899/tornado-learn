import tornado.httpserver
from tornado import ioloop,gen
import tornado.options
import tornado.web

from tornado.options import define, options
import os
import asyncio
import logging
from tornado_mysql import pools

define("port", default=8000, help="run on the given port", type=int)
POOL = pools.Pool(
    dict(host='127.0.0.1', port=3306, user='test', passwd='', db='mysql'),
    max_idle_connections=10,max_open_connections=50,
    max_recycle_sec=3)
#必须添加最大打开连接数。否则会mysql会报1040，超出最大连接数。

class IndexHandler(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self):
        cur = yield POOL.execute("SELECT host from user")

        self.write(str(cur.fetchall()))

if __name__ == "__main__":
    tornado.options.parse_command_line()
    logging.getLogger('tornado.access').disabled = True

    app = tornado.web.Application(handlers=[(r"/", IndexHandler)],
                static_path=os.path.join(os.path.dirname(__file__), "static"), debug=False)
    print(os.path.join(os.path.dirname(__file__), "static"))
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    print(asyncio.get_event_loop_policy())
    print(tornado.version)
    tornado.ioloop.IOLoop.instance().start()
