#Exercise 5: Write a program that prompts the user for a Celcius temperature, convert the temperature into Farenheit, and print out the converted temperature

celcius = float(input("Enter temperature in Celcius (ºC): "))
farenheit = (celcius * 9 / 5) + 32
print("Farenheit (ºF): ", farenheit)
