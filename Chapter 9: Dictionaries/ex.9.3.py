"""
Exercise 3: Write a program to read through a mail log, build a histogram using a
dictionary to count how many messages have come from each email address, and print
the dictionary.

You can download the file from:
https://www.py4e.com/code3/mbox-short.txt
"""

file = (input("Enter file name: "))
emails = {} # Dictionary

try:
    fhand = open(file)
except:
    print("Can't open file")
    quit()

for line in fhand:
    words = line.split()
    # print(words)
    # Ignore empty lines and lines that don't start with 'From'
    if len(words) == 0 or words[0] != 'From':
        continue
    else:
        email = words[1]
        # Make email = 1 if not in {}, else +1
        if email not in emails:
            emails[email] = 1
        else:
            emails[email] += 1
print(emails)
