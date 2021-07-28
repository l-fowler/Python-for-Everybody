"""
Exercise 2: Write a program to prompt for a file name, and then read through the file
and look for lines of the form:
X-DSPAM-Confidence: 0.8475

When you encounter a line that starts with "X-DSPAM-Confidence:" pull apart the line
to extract the floating-point number on the line. Count these lines and then compute
the total of the spam confidence values from these lines. When you reach the end of the
file, print out the average spam confidence.

Enter the file name: mbox.txt
Average spam confidence: 0.894128046745

Enter the file name: mbox-short.txt
Average spam confidence: 0.750718518519

You can download the files from:
www.py4e.com/code3/mbox-short.txt and www.py4e.com/code3/mbox.txt
"""
# Input file from user
fname = input("Enter file name: ")
# Try/Except
try:
    fhand = open(fname)
except:
    print("Couldn't find file")
    quit()

# Counter variables (sum of num_float and count of different num_float) = 0
sum = 0
count = 0
for line in fhand:
    line = line.rstrip()
    #line.find('') == -1 so that if 'X-DSPAM-Confidence' is not found will move back to the start of for loop
    if line.find('X-DSPAM-Confidence: ') == -1:
        continue
    else:
        # Find colon + 1 for number
        pos = line.find(':')
        num_str = line[pos+1:]
        num_float = float(num_str)
        sum = num_float + sum
        count = count + 1
#Average = sum / count
print(sum/count)

# Alternative for if/else in for loop
#     else:
#         index = len('X-DSPAM-Confidence: ')
#         num_str = line[index:]
#         num_float = float(num_str)
#         sum = num_float + sum
#         count = count + 1
#     #Average = sum / count
# print(sum/count)
