#Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters (hours and rate).

def computepay(h, r):
    if h <= 40:
        pay = h*r
    elif h > 40:
        pay = ((40*r)+((h-40)*r*1.5))
    return pay

hours = input("Enter the hours you worked this week: ")
rate = input("Enter the rate per hour worked: ")
try:
    fhours = float(hours)
    frate = float(rate)
except:
    print("Error, please enter numeric input")
    quit()

final_pay = computepay(fhours, frate)
print(final_pay)
