"""
Exercise 1: Write a simple program to simulate the operation of the grep command
on Unix. Ask the user to enter a regular expression and count the number of lines
that matched the regular expression:

$ python grep.py
Enter a regular expression: ^Author
mbox.txt had 1798 lines that matched ^Author

$ python grep.py
Enter a regular expression: ^X-
mbox.txt had 14368 lines that matched ^X-

$ python grep.py
Enter a regular expression: java$
mbox.txt had 4175 lines that matched java$

You can download the file from:
https://www.py4e.com/code3/mbox.txt
"""
import re
fname = input("Enter name of file: ")
try:
    fhand = open(fname)
except:
    print("Could not open file")
    quit()

reg_exp = input("Enter a regular expression: ")
str_reg_exp = str(reg_exp)

count = 0
for words in fhand:
    if re.findall(str_reg_exp, words):
        count += 1

print(fname + " had " + str(count) + " lines that matched " + str_reg_exp)
