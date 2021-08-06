"""
Exercise 2: Write a program that categorizes each mail message by which day of the
week the commit was done. To do this look for lines that start with “From”, then
look for the third word and keep a running count of each of the days of the week.
At the end of the program print out the contents of your dictionary (order does not
matter).

Sample Line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Sample Execution:
python dow.py
Enter a file name: mbox-short.txt
{'Fri': 20, 'Thu': 6, 'Sat': 1}

You can download the file from:
https://www.py4e.com/code3/mbox-short.txt
"""

# Make dictionary
days = {}

file = input("Enter file name: ")
try:
    fhand = open(file)
except:
    print("Can't open file")
    quit()
for line in fhand:
    words = line.split()
    # Ignore empty lines and lines that don't start with 'From'
    if len(words) == 0 or words[0] != 'From':
       continue
    else:
        day = words[2]
        # print(day)
        # Make day = 1 if not in {}, else +1
        if day not in days:
            days[day] = 1
        else:
            days[day] += 1
print(days)
