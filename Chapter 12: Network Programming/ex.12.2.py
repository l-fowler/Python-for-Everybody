"""
Exercise 2: Change your socket program so that it counts the number of characters
it has received and stops displaying any text after it has shown 3000 characters.
The program should retrieve the entire document and count the total number of
characters and display the count of the number of characters at the end of the
document.

You can download the file from:
http://data.pr4e.org/romeo.txt
"""

import socket

URL = input('Enter a URL: ')
URL_str = str(URL)
# print(URL_str)

# for characters in URL_str:
try:
    characters = URL_str.split('/')
    host_name = characters[2]
except:
    print("Could not open, check URL")
    quit()
# print(host_name)

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((host_name, 80))
cmd = ('GET '+ URL + ' HTTP/1.0\r\n\r\n').encode()
# cmd = f'GET {URL} HTTP/1.0\r\n\r\n'.encode() - alternate
mysock.send(cmd)

document = ''
count = 0
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    document = document + (data.decode())
    count = count + len(data)
mysock.close()

# only print document not the properties
position = document.find('\r\n\r\n')
# print document up to 3000 words
document = document[position+4:]
document = document[:3001]

print(document) # comment out just for character count and not document
print("Number of characters:", count)
