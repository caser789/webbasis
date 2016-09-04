def print_request_1():
    request = 'GET / HTTP/1.1\r\nHost: g.cn\r\n\r\nbody'
    print request

def print_request_2():
    request = """GET / HTTP/1.1
Host: g.cn

body"""
    print request

def main():
    # print_request_1()
    print_request_2()

if __name__ == '__main__':
    main()
