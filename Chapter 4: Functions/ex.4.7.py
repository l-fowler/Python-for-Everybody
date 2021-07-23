"""
Exercise 7: Rewrite the grade program from the previous chapter using a function
called computegrade that takes a score as its parameter and returns a grade as a
string.

Score   Grade
>= 0.9     A
>= 0.8     B
>= 0.7     C
>= 0.6     D
 < 0.6     F

Enter score: 0.95
A

Enter score: perfect
Bad score

Enter score: 10.0
Bad score

Enter score: 0.75
C

Enter score: 0.5
F
"""

# Define computegrade(score)
# Include if/else for scores and grades
def computegrade(score):
    if score >=0.9:
        grade = "Grade: A"
    elif score >= 0.8:
        grade = "Grade: B"
    elif score >= 0.7:
        grade = "Grade: C"
    elif score >= 0.6:
        grade = "Grade: D"
    elif score <0.6:
        grade = "Grade: F"
    return grade

# Input score
score = input("Enter score between 0.0 and 1.0: ")

# Try and Except
# Try float(score)
try:
    score = float(score)
# Except for int or str
except:
    print("Bad score")
    quit()

# Print "Bad score" if score > 1.0
if score > 1.0:
    print("Bad score")
    quit()

# Call function computegrade(score)
grade = computegrade(score)
print(grade)
