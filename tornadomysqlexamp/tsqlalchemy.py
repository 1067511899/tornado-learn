from __future__ import print_function

from tornado import  gen
from tornado_mysql import pools
import logging
import tornado.web


pools.DEBUG = True

POOL = pools.Pool(
    dict(host='192.168.1.155', port=3306, user='root', passwd='1qazxsw2!@', db='wpnbmdb', charset='utf8',),
    max_idle_connections=10, max_open_connections=90,
    max_recycle_sec=3)

@gen.coroutine
def main():
    cur = yield POOL.execute("SELECT * from zs_yjsf order by id")
    for row in cur:
        print(row)
    cur.close()

class IndexHandler(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self):
        cur = yield POOL.execute("SELECT * from zs_yjsf order by id limit 20")
        self.write(str(cur.fetchall()))
        cur.close()
        
        
if __name__ == "__main__":
    logging.getLogger('tornado.access').disabled = True

    app = tornado.web.Application(handlers=[(r"/", IndexHandler)], debug=False)

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(8888)
#     http_server.bind(80)
#     http_server.start(0)
#   很遗憾，上述代码不能在windows下运行，所以，tornado的多进程只能在linux底下运行。
#   把POOL 的定义放在这里，是因为POOL本身就会初始化一个eventloop。
#     POOL = pools.Pool(
#     dict(host='192.168.1.155', port=3306, user='root', passwd='1qazxsw2!@', db='wpnbmdb', charset='utf8',),
#     max_idle_connections=10, max_open_connections=90,
#     max_recycle_sec=3)

#     asyncio.set_event_loop_policy(asyncio.SelectorEventLoop)
# 设置任何eventloop都报错，被windows搞得没脾气。

    tornado.ioloop.IOLoop.instance().start()
