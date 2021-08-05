"""
Exercise 1: Write a program that reads the words in words.txt and stores them as keys in a 
dictionary. It doesn’t matter what the values are. Then you can use the in operator as a fast 
way to check whether a string is in the dictionary.

You can download the file from:
https://www.py4e.com/code3/words.txt
"""

fhand = open('words.txt')
words = dict() # {}
for word in fhand:
    key = word.split()
    # print('Debug:', key)
    for x in key:
        if x not in words:
            words[x] = 1
        else:
            words[x] = words[x] + 1
# print(words)
a = input("Check if word in file: ")
if a not in words:
    print("Could not find word in txt.file")
else:
    print(words.get(a))
