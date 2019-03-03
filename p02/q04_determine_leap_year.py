'''
4 (Determining leap year) q04_determine_leap_year.py
Write a program that prompts the user to enter a year and determines whether it is a leap year. A year is a leap year if it is divisible by 4 but
not 100, or is divisible by 400. 

Sample sessions:

Enter year: 2012
Leap

Enter year: 2013
Non-Leap '''

year = int(input("Enter year: "))
if year % 4 is 0 and year % 100 is not 0:
    print("Leap")
elif year % 400 is 0:
    print("Leap")
else:
    print("Non-Leap")
