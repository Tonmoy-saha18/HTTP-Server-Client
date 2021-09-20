import sys
from socket import *

# host = '127.0.0.1'
# port = 4444

s = socket(AF_INET, SOCK_STREAM)

s.connect((sys.argv[1], int(sys.argv[2])))
s.sendall("GET /{} HTTP/1.1\r\nHost: {}:{}\r\n\r\n".format(sys.argv[3], sys.argv[1], sys.argv[2]).encode())
message = s.recv(1024)
print(message.decode())

s.close()