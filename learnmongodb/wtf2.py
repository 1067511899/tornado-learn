import tornado
from tornado.ioloop import IOLoop
from motor.motor_tornado import MotorClient
import datetime
from tornado import web


class MainHandler(web.RequestHandler):

    def get(self):
        db = self.settings['db']
        db.collection.insert_one({'datetime':datetime.datetime.now()})
        

application = tornado.web.Application([
    (r'/', MainHandler)
])

server = tornado.httpserver.HTTPServer(application)
server.bind(8888)

# Forks one process per CPU.
server.start(0)

# Now, in each child process, create a MotorClient.
application.settings['db'] = MotorClient().test
IOLoop.current().start()
