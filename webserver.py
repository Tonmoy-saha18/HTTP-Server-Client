# server
# TCP Server Code
from socket import *

host = "127.0.0.1"
port = 4444

s = socket(AF_INET, SOCK_STREAM)

s.bind((host, port))

s.listen(5)

print("Listening for connections.. ")

while True:
    q, addr = s.accept()
    message = q.recv(1024)
    # print(addr)
    # print(q)
    #print(message)
    print("Connected with " + addr[0] + ':' + str(addr[1]))
    ls = message.split()
    request_file = ls[1][1:]
    #print(request_file)
    try:
        file = open(request_file, 'r')
        text = file.read()
        # q.send('HTTP/1.1 200 OK\r\n\r\n'.encode())
        data = ""
        for a in text:
            data += a
        # q.sendall(data.encode())
        q.sendall('HTTP/1.1 200 OK\r\n\r\n{}'.format(data).encode())
        q.close()
        file.close()
    except FileNotFoundError:
        # m = "Get /HTTP/1.1\r\n\r\n404 not found\r\n\r\n"
        # q.send('HTTP/1.1 200 OK\r\n\r\n'.encode())
        # q.sendall(m.encode())
        q.sendall('HTTP/1.1 200 OK\r\n\r\nGet /HTTP/1.1\r\n\r\n404 not found'.encode())
        q.close()

s.close()
