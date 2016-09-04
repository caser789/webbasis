import random
import socket

server = socket.socket()
host = ''
port = random.randint(2000, 3000)
addr = (host, port)

server.bind(addr)
print 'server at {}:{}'.format(host, port)

def from_file(path):
    filename = path.split('/')[-1]
    print 'fielname'
    print filename
    response = b'''HTTP/1.1 200 OK
Content-Type: image/gif

'''
    with open(filename, 'rb') as f:
        content = f.read()
        response += content
        return response

while True:
    server.listen(5)
    client, address = server.accept()
    request = client.recv(2048)
    request = request.decode('utf-8')
    line = request.split('\n')[0]
    path = line.split()[1]
    print 'path'
    print path
    if path in ['/doge1.gif', '/doge2.gif']:
        response = from_file(path)
    else:
        response = b'''HTTP/1.1 200 OK
Content-Type: text/html

<h1>Hello World!</h1>
<img src="/doge1.gif">
<img src="/doge2.gif">'''
    client.send(response)
    client.close()


