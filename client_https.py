import socket
import ssl

s = ssl.wrap_socket(socket.socket())

def parsed_url(url):
    """
    parse url
    return (protocol, host, port, path)
    """
    if url.startswith('https'):
        protocol = 'https'
    else:
        protocol = 'http'
    rest = url.split('://')[-1]

    host_port = rest.split('/', 1)[0]
    if ':' in host_port:
        host, port = host_port.split(':')
        port = int(port)
    else:
        host, port = host_port, 80

    path = rest.split(host_port)[-1]
    path = path if path else '/'
    return protocol, host, port, path


def socket_by_protocol(protocol):
    """
    return a socket instance according to protocol
    """


def response_by_socket(s):
    """
    s is a socket instance
    return all data in this socket
    """

def parsed_response(r):
    """
    parse response to get status code, headers, body
    status code: int
    headers: dict
    body: str
    """

def get(url):
    """
    use GET to request and return response
    """

def test_parsed_url():
    host = 'g.cn'
    port = 80
    path = '/'
    http = 'http'
    https = 'https'
    test_items = [
            ('http://g.cn', http, host, port, path),
            ('https://g.cn', https, host, port, path),
            ('http://g.cn/search', http, host, port, '/search'),
            ('http://g.cn:5555', http, host, 5555, path),
            ('g.cn', http, host, port, path),
            ('g.cn/', http, host, port, path),
            ]
    for item in test_items:
        assert item[1:] == parsed_url(item[0])



def test():
    test_parsed_url()


def main():
    url = 'https://movie.douban.com/top250'
    status_code, headers, body = get(url)
    print status_code, headers, body

if __name__ == '__main__':
    test()
    # main()
