import socket

# s = socket.socket(socket.AF_INET, socket.sock_STREAM)
s = socket.socket()

host = 'www.thebeijinger.com'
port = 80
addr = (host, port)
s.connect(addr)
print 'get socket name'
print s.getsockname()
http_request = """GET / HTTP/1.1
host: {}
Connection: close

""".format(host)
s.send(http_request.encode('utf-8'))
response = b''
while True:
    r = s.recv(1024)
    if len(r) == 0:
        break
    response += r
    print 'chunk'

print '*' * 40
print response.decode('utf-8')
with open('{}.html'.format(host), 'wb') as f:
    f.write(response)
print '*' * 40
