import xmlrpc.client  
import time
while True:
    try:
        s = xmlrpc.client.ServerProxy('http://192.168.1.157:8008')  
    except Exception as e:
        print(e)
        pass
    print (s.pow(2, 3))  # Returns 2**3 = 8  
    print (s.add(2, 3))  # Returns 5  
    print (s.div(5, 2))  # Returns 5//2 = 2  
    print(s.system.listMethods())
    exit()
    time.sleep(2)