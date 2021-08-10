"""
Exercise 2: This program counts the distribution of the hour of the day for each of
the messages. You can pull the hour from the “From” line by finding the time string
and then splitting that string into parts using the colon character. Once you have
accumulated the counts for each hour, print out the counts, one per line, sorted by
hour as shown below.

Sample line:
From stephen.marquard@uct.ac.az Sat Jan 05 09:14:16 2008

Sample Execution:
python timeofday.py
Enter a file name: mbox-short.txt
04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1

You can download the file from:
https://www.py4e.com/code3/mbox-short.txt and https://www.py4e.com/code3/mbox.txt
"""

fhand = input("Enter file name: ")
try:
    file = open(fhand)
except:
    print("Invalid file")
    quit()

hours = {}
for line in file:
    words = line.split()
    if len(words) == 0 or words[0] != 'From':
        continue
    else:
        time = words[5]
        hour = time.split(':')[0]
        # print(hour)
        if hour not in hours:
            hours[hour] = 1
        elif hour in hours:
            hours[hour] = hours[hour] + 1
# print(hours)
l = list()
for (key, value) in hours.items():
    l.append((key, value))

l.sort()

for (key, value) in l:
    print(key, value)
