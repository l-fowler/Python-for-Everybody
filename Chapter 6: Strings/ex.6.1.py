"""
Exercise 1: Write a while loop that starts at the last character in the string
and works its way backwards to the first character in the string, printing each
letter on a separate line, except backwards.
"""

# Input string from user
a = input("Enter word or sentence: ")

# Counter variable = 1
# Index will increase; -index will print from the end to the start of the input
index = 1
# While loop
while index < len(a):
    char = a[-index]
    print(char)
    # Index += 1
    index += 1
# Print first letter of string
print(a[0])
