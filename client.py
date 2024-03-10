import sys
from socket import *

#Client initiates a connection
HOST = "127.0.0.1"
PORT = 65432

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    
    #Data exhange
    s.sendall(b"hello world")
    data =s.recv(1024)
    
print(f"recieved{data}")
