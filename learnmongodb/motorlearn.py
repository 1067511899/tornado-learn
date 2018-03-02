
from tornado import ioloop, web, gen
import pymongo
import tornado
from _datetime import date
import datetime
from motor.motor_tornado import MotorClient

# client = pymongo.MongoClient('192.168.1.155', 27017)  # , maxPoolSize=1000, minPoolSize=200)
# db = client.test
db = MotorClient('192.168.1.155', 27017).test
item = {
    "Type":"Laptop",
    "ItemNumber":"1234444",
    "status":"In use",
    "Location":{
        "Department":"Development",
        "Building":"YH",
        },
    "Tags":["Laptop", "Development", "In use1"]
    }

 
class IndexHandler(web.RequestHandler):

    @gen.coroutine
    def get(self):
        result = yield db.collection.insert_one({'name': 'Randall'})
        print(result)
        self.write(str(result))

 
application = web.Application([
    (r'/', IndexHandler),
])
 
if __name__ == "__main__":
#     http_server = tornado.httpserver.HTTPServer(application)
# 
#     http_server.bind(8888)
# 
#     http_server.start(num_processes=0)  # tornado将按照cpu核数来fork进程
# 
#     tornado.ioloop.IOLoop.instance().start()
    application.listen(8888)
    ioloop.IOLoop.instance().start()
