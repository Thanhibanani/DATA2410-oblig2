from http.client import responses
from socket import *
import sys

def request(host, port):
    http_client =socket(AF_INET, SOCK_STREAM) 
    http_client.connect((host,port))
    http_client.send(b"GET / HTTP/1.1\r\nHost: " + host.encode() + b"\r\n\r\n")
    
    responses -http_client()