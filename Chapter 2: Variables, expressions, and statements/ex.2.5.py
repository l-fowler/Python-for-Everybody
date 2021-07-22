"""
Exercise 5: Write a program that prompts the user for a Celcius temperature, convert the temperature 
into Farenheit, and print out the converted temperature.
"""

# Input from user as a float
celcius = float(input("Enter temperature in Celcius (ºC): "))

# Equation for F to C
# (C * 9 / 5) + 32
farenheit = (celcius * 9 / 5) + 32
print("Farenheit (ºF): ", farenheit)
