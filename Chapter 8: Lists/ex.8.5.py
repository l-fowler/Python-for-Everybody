"""
Exercise 5: Minimalist Email Client.
Write a program to read through the mail box data and when you find line that starts
with “From”, you will split the line into words using the split function. We are
interested in who sent the message, which is the second word on the From line.

You can download the files from:
www.py4e.com/code3/mbox-short.txt
"""
# mbox-short.txt
file = input("Enter file name: ")
# Try and except
try:
    fhand = open(file)
except:
    print("Cannot open file")
    quit()

# Counter variables = 0
count = 0
for line in fhand:
    # Split line into words
    lines = line.split()
    # Ignore lines that don't start with 'From'
    if len(lines) == 0 or lines[0] != 'From':
        continue
    # +1 to count for line that starts with 'From'/has sent email
    count = count + 1
    # Print email of sender
    print(lines[1])
print("There were", count, "lines in the file with 'From' as the first word")
