"""
Exercise 2: Change your socket program so that it counts the number of characters
it has received and stops displaying any text after it has shown 3000 characters.
The program should retrieve the entire document and count the total number of
characters and display the count of the number of characters at the end of the
document.

You can download the file from:
http://www.py4e.com/code3/socket1.py
"""

import socket

URL = input('Enter a URL: ') # http://data.pr4e.org/romeo.txt
URL_str = str(URL)

try:
    characters = URL.split('/')
    host_name = characters[2]
    # print(host_name)

    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host_name, 80))
    cmd = ('GET '+ URL + ' HTTP/1.0\r\n\r\n').encode()
    # cmd = f'GET {URL} HTTP/1.0\r\n\r\n'.encode() #- alternate
    mysock.send(cmd)

    document = ''
    count = 0
    while True:
        data = mysock.recv(512)
        # print(len(data))
        if len(data) < 1:
            break
        document = document + data.decode()
        count += len(data)

    mysock.close()

    print(document[:3000])
    print("Character count:", count)
except:
    print("Improperly formatted or non-existent URL")
    quit()
