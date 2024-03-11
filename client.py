import sys
import socket

def http_request(server_ip, port, path):
    #Client initiates a HTTP request
    request=f"GET {path} HTTP/1.1\r\nHost: {server_ip}\r\nConnection: close\r\n\r\n"

    #Creates a TCP socket
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        try:
            
            #Connects to server
            s.connect((server_ip, port))
            #Sends the request
            s.sendall(request.encode())
            
            
            #Recieves the response
            response=b""
            while True:
                data=s.recv(1024)
                if not data:
                    break
                response += data
                
                #Displays the respons
                print(response.decode())
        except Exception as e:
            print(f"Error!: {e}")

#Runs the program using sys
if __name__=="__main__":
    if len(sys.argv) !=4:
        print("Usage: python client.py <server_ip> <port> <path>")
        sys.exit(1)
    server_ip=sys.argv[1]
    port =int(sys.argv[2])
    path=sys.argv[3]
    
http_request(server_ip, port, path)

