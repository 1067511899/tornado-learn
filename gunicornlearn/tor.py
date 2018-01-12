import tornado.ioloop
import tornado.web
import tornado.options

tornado.options.define('port', type=int, default='8080', help=u'port number')

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        print("get")
        self.write("Hello, world")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

def main():
    app = make_app()
    return app

app = main()

if __name__ == "__main__":
    print("starting..........")
    app.listen(8008)
    tornado.ioloop.IOLoop.current().start()