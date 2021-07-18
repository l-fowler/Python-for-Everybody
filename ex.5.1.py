#Exercise 1: Write a program which repeatedly reads nubers until the user enters "done". Once "done" is entered, print out the total, count, and average of the numbers.
#If the user enters anything other than a number, direct their mistake using try and except and print an error message and skip to the next number.

count = 0
total = 0
while True:
    num = input("Enter number: ")
    if num == 'done':
        print("Done")
        break
    else:
        try:
            fnum = float(num)
        except:
            print("Invalid input")
            continue
        total = total + fnum
        count = count + 1
print(total, count, total/count)
