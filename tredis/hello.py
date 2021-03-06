import tornado.httpserver
from tornado import gen
import tornado.options
import tornado.web

from tornado.options import define, options
import asyncio
import logging
from tornado_mysql import pools
import redis

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
#简单的应用，如果数据在redis里面，直接返回，否则查数据库。
#redis的连接只有一个，还不是异步的，但是性能比查mysql快至少一倍吧。
#异步redis太复杂，各种莫名其妙的错误，感觉没必要。
        result=c.get('user')
        if result:
            self.write(result)
        else:
            cur = yield POOL.execute("SELECT host from user")
            res=str(cur.fetchall())
            c.set('user',res)
            self.write(res)

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
    dict(host='127.0.0.1', port=3306, user='test', passwd='', db='mysql'),
    max_idle_connections=10, max_open_connections=90,
    max_recycle_sec=3)
    c = redis.StrictRedis(host='192.168.2.55', port=6379, db=0)

    
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