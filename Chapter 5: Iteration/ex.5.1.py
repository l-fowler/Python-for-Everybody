"""
Exercise 1: Write a program which repeatedly reads nubers until the user enters "done". 
Once "done" is entered, print out the total, count, and average of the numbers. If the 
user enters anything other than a number, direct their mistake using try and except and 
print an error message and skip to the next number.

Enter a number: 4
Enter a number: 5
Enter a number: bad data
Invalid input
Enter a number: 7
Enter a number: done
16 3 5.333333333333333
"""

# Count and total = 0
count = 0
total = 0
# While loop
while True:
    # Input number from user
    num = input("Enter number: ")
    if num == 'done':
        print("Done")
        break
    else:
        # Try and except
        # Try float(num)
        try:
            fnum = float(num)
        except:
            print("Invalid input")
            continue
        # total + fnum
        total = total + fnum
        # count + 1
        count = count + 1
# Print total, count, and average of the numbers
print(total, count, total/count)
