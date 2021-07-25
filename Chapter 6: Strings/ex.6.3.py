"""
Exercise 3: Encapsulate the code below in a function named count, and generalise it
so that it accepts the string and letter as arguments.

word = 'banana'
count = 0
for letter in word:
   if letter == 'a':
       count = count + 1
print(count)
"""

# Define count
def count(string, chosen_letter):
    """
    Counts the number of times a letter appears in a word.
    Example input:
        word = banana
        chosen_letter = a
    Example output:
        3
    """
    counter = 0
    for letter in string:
        if letter == chosen_letter:
            counter += 1
    return counter

# Word and letter inputs from user
word = input("Enter string: ")
chosen_letter = input("Enter letter you want to count: ")

# Ensure word and chosen_letter are not digits
if word.isdigit() or chosen_letter.isdigit():
    print("Input must not be a number")
    quit()

# Ensure letter is one character only
if len(chosen_letter) != 1:
    print("Input of letter must be a single character")
    quit()

# Put output into variable and print
letter_count = count(word, chosen_letter)
print(letter_count)
