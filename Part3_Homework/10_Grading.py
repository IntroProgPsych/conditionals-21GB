# You are tasked with creating a simple grading system for a class. 
# Write a Python program that takes a student's score as input
#  and calculates and prints its corresponding letter grade based on the following grading scale:

# 90 or above: A
# 80-89: B
# 70-79: C
# 60-69: D
# Below 60: F

score = int(input("Enter the student's score: "))

if score >= 90 and score <= 100:
    print("The letter grade is: A")
elif score >= 80 and score < 89:
    print("The letter grade is: B")
elif score >= 70 and score < 79:
    print("The letter grade is: C")
elif score >= 60 and score < 69:
    print("The letter grade is: D")
else:
    print("The letter grade is: F")