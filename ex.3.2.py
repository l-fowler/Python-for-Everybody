#Exercise 2: Rewrite your pay program using try and except so that your program hadnles non-numeric input gracefully by printing a message and axiting the program. The following shows two executions of the program:

hours = input("Enter the hours you worked this week: ")
rate = input("Enter the rate per hour worked: ")
try:
    fhours = float(hours)
    frate = float(rate)
except:
    print("Error, please enter numeric input")
    quit()

if fhours <= 40:
    pay = fhours*frate
    print(pay)

elif fhours > 40:
    above_40_fhours = fhours - 40
    pay = ((40*frate)+(above_40_fhours*frate*1.5))
    print(pay)
