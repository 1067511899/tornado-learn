import pymongo
# Connect to server
client = pymongo.MongoClient('192.168.1.155', 27017)
tmp = {
            "_id" : "<hostname>-<timestamp>-<increment>",
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
# Select the database
testdb = client.test
# Drop collection
print('Dropping collection person')
testdb.person.drop()
# Add a person
print('Adding a person to collection person')
employee = dict(name='Fred', age=30)
testdb.person.insert(employee)
# print(testdb.person._id)
testdb.collection.insert(tmp)
# Fetch the first entry from collection
person = testdb.person.find_one()
if person:
    print('Name: %s, Age: %s' % (person['name'], person['age']))
# Fetch list of all databases
print('DB\'s present on the system:')
for db in client.database_names():
    print(' %s' % db)
# Close connection
print('Closing client connection')
client.close()

if __name__ == '__main__':
    pass
