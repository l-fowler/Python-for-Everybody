"""
Exercise 4: Change the urllinks.py program to extract and count paragraph (p) tags
from the retrieved HTML document and display the count of the paragraphs as the output
of your program. Do not display the paragraph text, only count them. Test your program
on several small web pages as well as some larger web pages.

To run this, download the BeautifulSoup zip file http://www.py4e.com/code3/bs4.zip
and unzip it in the same directory as this file

You can download the file from:
http://www.py4e.com/code3/urllinks.py
"""

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter URL: ') # http://data.pr4e.org/romeo.txt
                           # http://data.pr4e.org/mbox.txt

count = 0
try:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all of the anchor tags
    tags = soup('p')
    for tag in tags:
        count += 1
except:
    print("Could not open, check URL")
    quit()

print("Number of paragraphs:", count)
