"""
Exercise 6: Rewrite the program that prompts the user for a list of numbers and prints
out the maximum and minimum of the numbers at the end when the user enters “done”. Write
the program to store the numbers the user enters in a list and use the max() and min()
functions to compute the maximum and minimum numbers after the loop completes.
"""

# List
num_list = list()

# While loop - ask for number or 'done'
while True:
    num = input("Enter a number, or 'done' when you're complete: ")
    # If/else
    # If 'done', break from while loop
    if num == 'done':
        break
    # Else - continue with number input, or ignore if other (try/except)
    else:
        try:
            float_num = float(num)
        except:
            # Continue with wrong input
            print("Input must be a number, or 'done' when you're complete")
            continue
        # Append number to list
        num_list.append(float_num)
# Print max and min
print("Maximum:", max(num_list))
print("Minimum:", min(num_list))
