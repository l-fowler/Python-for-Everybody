"""
Exercise 2: Write a program to look for lines of the form:

New Revision: 39772

Extract the number from each of the lines using a regular expression and the findall()
method. Compute the average of the numbers and print out the average as an integer.

Enter file:mbox.txt
38549

Enter file:mbox-short.txt
39756

You can download the files from:
https://www.py4e.com/code3/mbox.txt and https://www.py4e.com/code3/mbox-short.txt
"""

import re

fname = input("Enter file name: ")
try:
    fhand = open(fname)
except:
    print("Couldn't find file", fname)
    quit()

list = []

for line in fhand:
    line = line.rstrip()
    NR_numbers = re.findall('^New Revision: ([0-9.]+)', line)
    # print("Debug:", NR_numbers)
    for number in NR_numbers:
        number = float(number)
        list = list + [number]
        # print("Debug:", list)
total = sum(list)
count = float(len(list))
ave = total/count
# print(ave)
format_ave = "{:.2f}".format(ave)
print(format_ave)
