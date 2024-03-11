import sys
from socket import *

def http_request(server_ip, port, path):
    #Client initiates a HTTP request
    request=f"GET {path} HTTP/1.1\r\nHost: {server_ip}\r\nConnection: close\r\n\r\n"

    #Creates a TCP socket
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        try:
            s.connect((server_ip, port))
            s.sendall(request.encode())
            
            response=b""
            while True:
                data=s.recv(1024)
                if not data:
                    break
                response += data
                
                print(response.decode())
        except Exception as e:
            print(f"Error!: {e}")

if __name__=="__main__":
    if len(sys.argv) !=4:
        print("Usage: python http_client.py <server_ip> <port> <path>")
        sys.exit(1)
    server_ip=sys.argv[1]
    port =int(sys.argv[2])
    path=sys.argv[3]
    
http_request(server_ip,port,path)

