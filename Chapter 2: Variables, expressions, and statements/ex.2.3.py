"""
Exercise 3: Write a program to prompt the user for hours and rate per hour to compute gross pay.

Enter Hours: 35
Enter Rate: 2.75
Pay: 96.25
"""

# Input how many hours and rate
# Ensure input is float
hours = float(input("Enter how many hours you worked: "))
rate = float(input("Enter how much you are paid per hour: "))

# Calculate pay
pay = hours * rate
print(pay)
