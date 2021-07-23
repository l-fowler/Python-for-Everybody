"""
Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate 
for hours worked above 40 hours.

Enter Hours: 45
Enter Rate: 10
Pay: 475.0
"""

# Input hours and rate
hours = float(input("Enter the hours you worked this week: "))
rate = float(input("Enter the rate per hour worked: "))

# Hours are ≤ 40 * rate
if hours <= 40:
    pay = hours*rate
    print(pay)
# Hours > 40 * rate * 1.5
elif hours > 40:
    above_40_hours = hours - 40
    pay = ((40*rate)+(above_40_hours*rate*1.5))
    print(pay)
