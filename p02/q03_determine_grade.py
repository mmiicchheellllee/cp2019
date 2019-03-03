'''
3 (Determining grade) q03_determine_grade.py
Write a program that prompts the user to enter a score between 0 and 100 inclusive. The grading system is as follows:
A: 70 - 100
B: 60 - 69
C: 55 - 59
D: 50 - 54
E: 45 - 49
S: 35 - 44
U: 0 - 34

Sample sessions:

Enter score: 73
A 

Enter Score: -1
Invalid! Score must be within 0 - 100. '''

# grading system


score = int(input("Enter score: "))
if score >= 0 and score <= 34:
    print("U")
elif score >= 35 and score <= 44:
    print("S")
elif score >= 45 and score <= 49:
    print("E")
elif score >= 50 and score <= 54:
    print("D")
elif score >= 55 and score <= 59:
    print("C")
elif score >= 60 and score <= 69:
    print("B")
elif score >= 70 and score <= 100:
    print("A")
else:
    print("Invalid! Score must be within 0 - 100.")
