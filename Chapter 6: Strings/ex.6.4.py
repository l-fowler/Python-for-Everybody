"""
Exercise 4: There is a string method called count that is similar to the function
in the previous exercise.
Write an invocation that counts the number of times the letter a occurs in “banana”.
"""
word = 'banana'
letter_count = word.count('a')
print(letter_count)

# Alternative
# Input word and letter from user
word = input("Enter word: ")
letter = input("Enter letter: ")

# Ensure word and chosen_letter are not digits
if word.isdigit() or letter.isdigit():
    print("Input must not be a number")
    quit()

# Ensure letter is one character only
if len(letter) != 1:
    print("Input of letter must be a single character")
    quit()

# Use method .count()
letter_count = word.count(letter)
print(letter_count)
