import argparse, socket
import logging
from datetime import datetime
import signal

MAX_BYTES = 65535

def server(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # SOCK_DGRAM表示在ip网络上使用UDP协议
    sock.bind(('127.0.0.1', port))
    print('Listening at {}'.format(sock.getsockname()))
    try:
        while True:
            data, address = sock.recvfrom(MAX_BYTES)
            text = data.decode('ascii')
            print('The client at {} sys {!r}'.format(address, text))
            text = 'Yout data was {} bytes long'.format(len(data))
            data = text.encode('ascii')
            sock.sendto(data, address)
    except KeyboardInterrupt:
        pass


def client(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    text = 'The time is {}'.format(datetime.now())
    data = text.encode('ascii')
    sock.sendto(data, ('127.0.0.1', port))
    print('The OS assigned me the address {}'.format(sock.getsockname()))
    data, address = sock.recvfrom(MAX_BYTES) # danger
    text = data.decode('ascii')
    print('The server {} replied {!r}'.format(address, text))

# 这里可以用来做特殊中断的时候一些处理，例如：发送告警邮件、处理未完结的任务
def handler(signum, frame):
    print('handler is runing...')
    exit()

if __name__ == '__main__':
    signal.signal(signal.SIGINT, handler)
    signal.signal(signal.SIGHUP, handler)
    signal.signal(signal.SIGTERM, handler)

    choices = {'client': client, 'server': server}
    parser = argparse.ArgumentParser(description='Send and receive UDP locally')
    parser.add_argument('role', choices=choices, help='which role to play')
    parser.add_argument('-p', metavar='PORT', type=int, default=1060, help='UDP port(default 1060)')
    args = parser.parse_args()
    function = choices[args.role]
    function(args.p)