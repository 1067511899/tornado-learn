import tornado.httpserver
from tornado import gen
import tornado.options
import tornado.web

from tornado.options import define, options
import os
import asyncio
import logging
from tornado_mysql import pools
import tornadoredis
import time

# 不要在意混乱的import风格。


define("port", default=8000, help="run on the given port", type=int)

# 必须添加最大打开连接数。否则会mysql会报1040，超出最大连接数。
# wrk -c 600会报错：linux底下没这个问题。
# platform\select.py", line 63, in poll
#     self.read_fds, self.write_fds, self.error_fds, timeout)
# ValueError: too many file descriptors in select()

class IndexHandler(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self):
        c = tornadoredis.Client(host='192.168.2.55')

#         cur = yield POOL.execute("SELECT host from user")
        t=str(time.time())
        sqlstr="insert into normalinfo(title,detail) values ('"+t+"','"+t+"')"
        cur=yield POOL.execute(sqlstr)
        cur=yield POOL.execute("select last_insert_id()")
#         c.
        self.write(str(cur.fetchall()))

if __name__ == "__main__":
    tornado.options.parse_command_line()
    logging.getLogger('tornado.access').disabled = True

    app = tornado.web.Application(handlers=[(r"/", IndexHandler)], debug=False)

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
#   http_server.bind(options.port)
#   http_server.start(0)
#   很遗憾，上述代码不能在windows下运行，所以，tornado的多进程只能在linux底下运行。
#   把POOL 的定义放在这里，是因为POOL本身就会初始化一个eventloop。

    POOL = pools.Pool(
    dict(host='127.0.0.1', port=3306, user='test', passwd='', db='test'),
    max_idle_connections=10, max_open_connections=90,
    max_recycle_sec=3)
    
#     asyncio.set_event_loop_policy(asyncio.SelectorEventLoop)
# 设置任何eventloop都报错，被windows搞得没脾气。
    print(asyncio.get_event_loop_policy())
    print(tornado.version)
    tornado.ioloop.IOLoop.instance().start()


#理论上，如果瓶颈不是数据库的话，那么tornado的性能（rps），是单核的性能*cpu的核数。
#超出核数的进程数显然不能带来明显的性能改变。
#如果使用mysql workbench来监控mysql的性能的话，那么重启mysql服务器后，需要重新连接
#mysql服务器，否则服务器的状态就不能正确显示。
#insert 的性能明显下降，大概只有100左右的qps，还有大量超时，具体原因不明。