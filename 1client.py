import socket

# s = socket.socket(socket.AF_INET, socket.sock_STREAM)
s = socket.socket()

host = 'g.cn'
port = 80
addr = (host, port)
s.connect(addr)
print 'get socket name'
print s.getsockname()
http_request = """GET / HTTP/1.1
host: {}

""".format(host)
s.send(http_request.encode('utf-8'))
http_response = s.recv(1023)
print '*' * 40
print http_response.decode('utf-8')
