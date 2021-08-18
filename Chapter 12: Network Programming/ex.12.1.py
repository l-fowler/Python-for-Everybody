"""
Exercise 1: Change the socket program socket1.py to prompt the user for the URL
so it can read any web page. You can use split('/') to break the URL into its
component parts so you can extract the host name for the socket connect call.
Add error checking using try and except to handle the condition where the user
enters an improperly formatted or non-existent URL.

You can download the files from:
http://www.py4e.com/code3/socket1.py and http://data.pr4e.org/romeo.txt
"""
import socket

URL = input('Enter a URL: ') # http://data.pr4e.org/romeo.txt
URL_str = str(URL)
# print(URL_str)

try:
    characters = URL_str.split('/')
    host_name = characters[2]
except:
    print("Could not open URL")
    quit()
# print(host_name)


mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((host_name, 80))
cmd = ('GET '+ URL + ' HTTP/1.0\r\n\r\n').encode()
# cmd = f'GET {URL} HTTP/1.0\r\n\r\n'.encode() #- alternate
mysock.send(cmd)
print(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()
