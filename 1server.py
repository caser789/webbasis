import random
import socket

server = socket.socket()
host = ''
port = random.randint(2000, 3000)
addr = (host, port)

server.bind(addr)
print 'server at {}:{}'.format(host, port)

while True:
    server.listen(5)
    client, address = server.accept()
    print 'client address'
    print address
    request = client.recv(2048)
    print 'request'
    print request.decode('utf-8')
    response = 'hello world'.encode('utf-8')
    client.send(response)
    client.close()
