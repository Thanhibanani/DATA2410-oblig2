import sys
from socket import *
import threading


def client_handle(connectionSocket):
    try:
        #Receive HTTP requests 
        message = connectionSocket.recv(1024)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()

        # Send one HTTP header line into socket
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())

        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
            connectionSocket.close()

    except IOError:
        # Send response message for file not found
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        connectionSocket.send(
            "<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n".encode())
        # Close client socket
        connectionSocket.close()
serverSocket =socket(AF_INET, SOCK_STREAM)
serverPort = 6789
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('Server is ready to receive')

try:
    while True:
        connectionSocket,addr =serverSocket.accept()
        #Starts a new thread to handle requests
        threading.Thread(target=client_handle, args =(connectionSocket,)).start()
finally:
    #Close the server socket
    serverSocket.close()
   