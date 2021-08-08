"""
Exercise 4: Add code to the above program to figure out who has the most messages
in the file. After all the data has been read and the dictionary has been created,
look through the dictionary using a maximum loop.

You can download the files from:
https://www.py4e.com/code3/mbox-short.txt and https://www.py4e.com/code3/mbox.txt
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
# print(emails)

# Tuples
# Check max
high = [(value, key) for key, value in emails.items()]
print(max(high))

# Check min
low = [(value, key) for key, value in emails.items()]
print(min(low))
