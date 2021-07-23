"""
Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and
create a function called computepay which takes two parameters (hours and rate).

Enter Hours: 45
Enter Rate: 10
Pay: 475.0
"""

# Define computepay(hours, rate)
def computepay(hours, rate):
    if hours <= 40:
        pay = hours*rate
    elif hours > 40:
        pay = ((40*rate)+((hours-40)*rate*1.5))
    return pay

# Input hours and rate
hours = input("Enter the hours you worked this week: ")
rate = input("Enter the rate per hour worked: ")

# Try and Except
# Try float(hours) and float(rate)
try:
    fhours = float(hours)
    frate = float(rate)
except:
    print("Error, please enter numeric input")
    quit()

final_pay = computepay(fhours, frate)
print(final_pay)
