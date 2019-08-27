import argparse, socket

def recvall(sock, length):
    data = b''
    while len(data) < length:
        more = sock.recv(length - len(data))
        if not more:
            raise EOFError('was expecting %d bytes but only received %d bytes before the socket closed' % (length, len(data)))
        data += more
    return data

def server(interface, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # 这里参数表明使用操作系统还保留着的准备断开的套接字地址。不然会提示端口已占用
    sock.bind((interface, port))
    sock.listen(1) # 这里的1指明了处于等待的连接的最大数目, 如果还未创建会被压入栈中。超过数目会被抛掉
    print('Listening at', sock.getsockname())
    while True:
        sc, sockname = sock.accept() # 为连接创建套接字
        print('We have accepted a connection from', sockname)
        print(' Socket name:', sc.getsockname())
        print(' Socket peer:', sc.getpeername()) # 获取客户端的地址
        message = recvall(sc, 16)
        print(' Incoming sixteen-octet message:', repr(message))
        sc.sendall(b'Farewell, client')
        sc.close()
        print(' Reply sent, socket closed')


def client(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    print('Client has been assigned socket name', sock.getsockname())
    sock.sendall(b'Hi there, server')
    reply = recvall(sock, 16)
    print('The server said', repr(reply))
    sock.close()


if __name__ == '__main__':
    choices = {'client': client, 'server': server}
    parser = argparse.ArgumentParser(description='Send and receive over TCP')
    parser.add_argument('role', choices=choices, help='which role to play')
    parser.add_argument('host', help='interface the server listens at; host the client sends to')
    parser.add_argument('-p', metavar='PORT', type=int, default=1060, help='TCP port(default 1060)')
    args = parser.parse_args()
    function = choices[args.role]
    function(args.host, args.p)





