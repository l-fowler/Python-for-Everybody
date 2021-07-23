"""
Exercise 2: Write another program that prompts for a list of numbers as above and at 
the end prints out both the maximum and minimum of the numbers instead of the average.
"""

# Counter variables = 0
i = 0
m = 0
# While loop
while True:
    # Input number from user
    num = input("Enter number: ")
    if num == 'done':
        break
    else:
        # Try and except
        # Try float(num)
        try:
            fnum = float(num)
        except:
            print("Invalid input")
            continue
        # If/else
        # If i==0, let fnum = smallest_num
        if i == 0:
            smallest_num = fnum
            i=i+1
        # Compare fnum < smallest_num
        elif fnum < smallest_num:
            smallest_num = fnum
        else:
            # If m==0, let fnum = largest_num
            if m == 0:
                largest_num = fnum
                m=m+1
            # Compare fnum > largest_num
            elif fnum > largest_num:
                largest_num = fnum

# Print minimum and maximum numbers
print("Minimum number:", smallest_num, "Maximum number:", largest_num)
