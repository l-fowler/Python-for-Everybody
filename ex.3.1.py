#Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.

hours = int(input("Enter the hours you worked this week: "))
rate = float(input("Enter the rate per hour worked: "))

if hours <= 40:
    pay = hours*rate
    print(pay)

elif hours > 40:
    above_40_hours = hours - 40
    pay = ((40*rate)+(above_40_hours*rate*1.5))
    print(pay)
