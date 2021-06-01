#Exercise 3: Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message. If the score is between 0.0 and 1.0, print a grade using the following table:
# Score   Grade
#>= 0.9     A
#>= 0.8     B
#>= 0.7     C
#>= 0.6     D
# < 0.6     F
def score(num):
    if num >=0.9:
        grade = "Grade: A"
    elif num >= 0.8:
        grade = "Grade: B"
    elif num >= 0.7:
        grade = "Grade: C"
    elif num >= 0.6:
        grade = "Grade: D"
    elif num <0.6:
        grade = "Grade: F"
    return grade

s = input("Enter score between 0.0 and 1.0: ")
try:
    s = float(s)
except:
    print("Bad score")
    quit()

grade = score(s)
print(grade)
