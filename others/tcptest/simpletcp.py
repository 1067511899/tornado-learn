import socket

target_host = 'www.yhsoft.com'
target_port = 80

text = '''
GET / HTTP/1.1
Host: 192.168.1.157:8000
Connection: keep-alive
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36
\r\n\r\n
'''

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host, target_port))
client.send(text.encode())
response = client.recv(1024)
print(response)
client.close()
