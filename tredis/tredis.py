'''
Created on 2017/12/28

@author: limengwei

Some examples about tornado and redis.
code from https://github.com/leporo/tornado-redis/blob/master/demos/simple/app.py
修改，使之能够在py3底下运行。
显然只能在tornado4.X版本运行，5.0a1修改了接口，导致无法运行。
'''
import tornadoredis
import tornado.httpserver
import tornado.web
import tornado.ioloop
import tornado.gen
import logging


logging.basicConfig(level=logging.DEBUG)

log = logging.getLogger('app')


class MainHandler(tornado.web.RequestHandler):

    @tornado.web.asynchronous
    @tornado.gen.engine
    def get(self):
        c = tornadoredis.Client(host='192.168.2.55')
        foo = yield tornado.gen.Task(c.get, 'foo')
        bar = yield tornado.gen.Task(c.get, 'bar')
        zar = yield tornado.gen.Task(c.get, 'zar')
        self.set_header('Content-Type', 'text/html')
        self.render("template.html", title="Simple demo",
                    foo=foo, bar=bar, zar=zar)


application = tornado.web.Application([
    (r'/', MainHandler),
])


@tornado.gen.engine
def create_test_data():
    c = tornadoredis.Client(host='192.168.2.55')
    with c.pipeline() as pipe:
        pipe.set('foo', 'Lorem ipsum #1', 12 * 60 * 60)
        pipe.set('bar', 'Lorem ipsum #2', 12 * 60 * 60)
        pipe.set('zar', 'Lorem ipsum #3', 12 * 60 * 60)
        yield tornado.gen.Task(pipe.execute)
    print ('Test data initialization completed.')


if __name__ == '__main__':
    # Start the data initialization routine
    create_test_data()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()