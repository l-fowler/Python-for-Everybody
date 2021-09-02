"""
Exercise 3: Use urllib to replicate the previous exercise of (1) retrieving the
document from a URL, (2) displaying up to 3000 characters, and (3) counting the
overall number of characters in the document. Don’t worry about the headers for
this exercise, simply show the first 3000 characters of the document contents.

You can download the file from:
http://www.py4e.com/code3/urllib1.py
"""
import urllib.request

URL = input('Enter a URL: ') # http://data.pr4e.org/romeo.txt
                             # http://data.pr4e.org/mbox.txt

document = ''
count = 0
limit = 3000
try:
    fhand = urllib.request.urlopen(URL)
    for line in fhand:
        line = line.decode().strip('\n') # excludes new line from count
        count += len(line)
        if count <= limit:
            print(line) # print line if < 3000 characters
except:
    print("Could not open, check URL")
    quit()

print("\n" + "Number of characters:", count) # excluding new line as a character
