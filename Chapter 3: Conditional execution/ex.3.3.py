"""
Exercise 3: Write a program to prompt for a score between 0.0 and 1.0. If the score is out of 
range, print an error message. If the score is between 0.0 and 1.0, print a grade using the 
following table:

 Score   Grade
>= 0.9     A
>= 0.8     B
>= 0.7     C
>= 0.6     D
 < 0.6     F

Run the program repeatedly as shown to test the various different values for input.
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
# Input score
score = input("Enter score between 0.0 and 1.0: ")
# Try and except
# Try float score
try:
    score = float(score)
except:
    print("Bad score")
    quit()
# If/else
# If score > 1.0
if score > 1.0:
    print("Bad score")
# Elif scores and grades from table
elif score >=0.9:
    print("Grade: A")
elif score >= 0.8:
    print("Grade: B")
elif score >= 0.7:
    print("Grade: C")
elif score >= 0.6:
    print("Grade: D")
elif score <0.6:
    print("Grade F")

