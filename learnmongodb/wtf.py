import tornado
from tornado.ioloop import IOLoop
from motor.motor_tornado import MotorClient
import datetime
from tornado import web


class MainHandler(web.RequestHandler):

    def get(self):
        db = self.settings['db']
        tmp = {
            "server" : "<hostname><:port>",
            "clientAddr" : "127.0.0.1:63381",
            "time" : "2012-12-11T14:09:21.039Z",
            "what" : "split",
            "ns" : "<database>.<collection>",
            "details" : {
                "before" : {
                    "min" : {
                        "<database>" : { 'minKey' : 1 }
                        },
                    "max" : {
                        "<database>" : { 'maxKey' : 1 }
                        },
                    "lastmod" : 1000,
                    "lastmodEpoch" :"000000000000000000000000"
                    },
                "left" : {
                    "min" : {
                        "<database>" : { 'minKey ': 1 }
                        },
                    "max" : {
                        "<database>" : "<value>"
                        },
                    "lastmod" : 1000
                    },
                "right" : {
                    "min" : {
                        "<database>" : "<value>"
                        },
                    "max" : {
                        "<database>" : {' maxKey ': 1 }
                        },
                    "lastmod" : 1000
                    }
                }
            }
        db.collection.insert_one(tmp)
        

application = tornado.web.Application([
    (r'/', MainHandler)
])

server = tornado.httpserver.HTTPServer(application)
server.bind(8888)

# Forks one process per CPU.
server.start(0)

# Now, in each child process, create a MotorClient.
application.settings['db'] = MotorClient('192.168.1.155', 27017).test
IOLoop.current().start()
