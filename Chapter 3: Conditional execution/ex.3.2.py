"""
Exercise 2: Rewrite your pay program using try and except so that your program 
handles non-numeric input gracefully by printing a message and axiting the 
program. The following shows two executions of the program:

Enter Hours: 20
Enter Rate: nine
Error, please enter numeric input

Enter Hours: forty
Error, please enter numeric input
"""
# Input hours and rate
hours = input("Enter the hours you worked this week: ")
rate = input("Enter the rate per hour worked: ")

# Try and except
# Try float of hours and rate
try:
    fhours = float(hours)
    frate = float(rate)
except:
    print("Error, please enter numeric input")
    quit()

# Hours ≤ 40 * rate
if fhours <= 40:
    pay = fhours*frate
    print(pay)
# Hours > 40 * rate * 1.5
elif fhours > 40:
    above_40_fhours = fhours - 40
    pay = ((40*frate)+(above_40_fhours*frate*1.5))
    print(pay)
