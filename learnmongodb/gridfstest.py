import pymongo
import gridfs
# Connect to server
client = pymongo.MongoClient('192.168.1.155', 27017)
# Select the database
testdb = client.test
fs = gridfs.GridFS(testdb)

f = open("c:/tmp/hosts", 'r+b')

uid = fs.put(f, encoding='utf-8')

print(uid)
client.close()
