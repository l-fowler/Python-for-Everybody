"""
Exercise 1: Run the program on your system and see what numbers you get. Run the program
more than once and see what numbers you get.

>>> random.randint(5, 10)
5
>>> random.randint(5, 10)
9

>>> t = [1, 2, 3]
>>> random.choice(t)
2
>>> random.choice(t)
3
"""
# Import 'random' module
import random

# Input low and high numbers
low = input("Enter low number: ")
high = input("Enter high number: ")

# Try and except
# Try int(low) and int(high)
try:
    low = int(low)
    high = int(high)
# Except must be integers
except:
    print("Cannot find random number. Inputs must be integers")
    quit()

# .randint(low, high) returns random number between and including low and high numbers
random_num = random.randint(low, high)
print(random_num)

# list and .choice(list) returns random number from list
list = [1, 2, 3]
random_num2 = random.choice(list)
print(random_num2)
