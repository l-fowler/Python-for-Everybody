"""
Exercise 3: Write a program that reads a file and prints the letters in decreasing
order of frequency. Your program should convert all the input to lower case and
only count the letters a-z. Your program should not count spaces, digits,
punctuation, or anything other than the letters a-z. Find text samples from several
different languages and see how letter frequency varies between languages. Compare
your results with the tables at https://wikipedia.org/wiki/Letter_frequencies.
"""

fname = input("Enter file name: ")
try:
    file = open(fname)
except:
    print("Couldn't find file")
    quit()

# read the file as a single string
words = file.read()
# convert string into lower case
words = words.lower()

letters = list()
for i in words :
    if i.isalpha() == True :
        letters.append(i)
letters.sort()

count = {}
for letter in letters:
    if letter not in count:
        count[letter] = 1
    else:
        count[letter] += 1

l = list()
for (key, value) in count.items():
    l.append((value, key))
    l.sort(reverse=True)
for (value, key) in l:
    print(key, value)
