from kafka import KafkaProducer
from kafka.errors import KafkaError
import random

producer = KafkaProducer(bootstrap_servers=['192.168.1.157:9092'])

# Asynchronous by default
# future = producer.send('test', b'raw_bytes')
# 
# # Block for 'synchronous' sends
# try:
#     record_metadata = future.get(timeout=10)
# except KafkaError:
#     # Decide what to do if produce request failed...
#     
#     pass

# Successful result returns assigned partition and offset
# print (record_metadata.topic)
# print (record_metadata.partition)
# print (record_metadata.offset)
# 
# # produce keyed messages to enable hashed partitioning
# producer.send('test', key=b'foo', value=b'bar')

# encode objects via msgpack

# produce asynchronously
import time
tmp = str(time.time())
for _ in range(1000000):
    producer.send('test', key=str(random.randint(1, 100000000)).encode('utf_8'), value=tmp.encode(encoding='utf_8', errors='strict'))

# block until all async messages are sent
producer.flush()

# configure multiple retries
# producer = KafkaProducer(retries=5)
