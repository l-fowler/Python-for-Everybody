"""
Exercise 1: Revise a previous program as follows: Read and parse the “From” lines and
pull out the addresses from the line. Count the number of messages from each person
using a dictionary.
After all the data has been read, print the person with the most commits by creating a
list of (count, email) tuples from the dictionary. Then sort the list in reverse order
and print out the person who has the most commits.

Sample line:
From stephen.marquard@uct.ac.az Sat Jan 05 09:14:16 2008

Enter a file name: mbox-short.txt
cwen@iupui.edu 5

Enter a file name: mbox.txt
zqian@umich.edu 195

You can download the file from:
https://www.py4e.com/code3/mbox-short.txt and https://www.py4e.com/code3/mbox.txt
"""

fhand = input("Enter file name: ")
try:
    file = open(fhand)
except:
    print("Can't find file")
    quit()

emails = {}
for line in file:
    words = line.split()
    if len(words) == 0 or words[0] != 'From':
        continue
    else:
        email = words[1]
        # print(email)
        if email not in emails:
            emails[email] = 1
        elif email in emails:
            emails[email] += 1
# print(emails)

l = list()
for (k, v) in emails.items():
    l.append((v, k))

# print(l)
l.sort(reverse=True)

for (k, v) in l[:1]:
    # can print (v, k) or (k, v)
    print(v, k)
