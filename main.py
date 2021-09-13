import socket
from urllib.parse import urlparse
import re 
import os 

socket.setdefaulttimeout = 0.5 
os.environ['no_proxy'] = '127.0.0.1,localhost'
link_regex = re.compile('<a\s*href=[\'|"](.*?)[\'"].*?>')
CRLF = "\r\n\r\n"

def GET(url): 
    """ HTTP GET method """
    url = urlparse(url)
    path = url.path
    HOST = url.netloc  
    path = "/" if path == "" else path 
    PORT = 80 
    # Create an INET, STREAMing socket -> TCP connection 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
    # set up TCP cnxn 
    s.connect((HOST,PORT))
    msg = f'GET {path} HTTP/1.0\r\nHost: www.sketchyactivity.com{CRLF}'
    
    # Send GET request, encode as binary representation
    s.send(msg.encode())

    data_append = ''
    
    # wait for server response 
    while True: 
        data = (s.recv(100000000))
        if not data: break 
        else: 
            data_append = data_append, repr(data)

    # shut down and close TCP connection and socket 
    s.shutdown(1) 
    s.close()
    print('Received', data_append)

GET('https://www.sketchyactivity.com/')
