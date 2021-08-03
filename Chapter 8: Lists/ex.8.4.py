"""
Exercise 4: Find all unique words in a file. Create a list of unique words, which will
contain the final result. Write a program to open the file romeo.txt and read it line
by line. For each line, split the line into a list of words using the split function.
For each word, check to see if the word is already in the list of unique words. If the
word is not in the list of unique words, add it to the list. When the program completes,
sort and print the list of unique words in alphabetical order.

You can download the files from:
www.py4e.com/code3/romeo.txt
"""
# Create list
unique_list = list()

fhand = open('romeo.txt')
# Read file
file = fhand.read()
# Split words
word = file.split()
for x in word:
    # Check if in list
    if x in unique_list:
        continue
    else:
        # Append new words
        unique_list.append(x)
# Sort list so each word starting with same letter - capital or lower case - has same value
sorted_list = sorted(unique_list, key=lambda L: (L.lower(), L))
print(sorted_list)
