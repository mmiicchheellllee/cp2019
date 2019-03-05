'''
5 (Finding the number of days in a month) q05_find_month_days.py 
Write a program that prompts the user to enter the month and year, and displays the number of days in the month. For example, 
if the user entered month 2 and year 2000, the program should display that February 2000 has 29 days. If the user entered 
month 3 and year 2005, the program should display that March 2005 has 31 days. '''

from calendar import monthrange
month = eval(input("Enter month: "))
year = eval(input("Enter year: "))
days = monthrange(year, month)
if month == 1:
    print("January", year, "has", days[1], "days")
elif month == 2:
    print("February", year, "has", days[1], "days")
elif month == 3:
    print("March", year, "has", days[1], "days")
elif month == 4:
    print("April", year, "has", days[1], "days")
elif month == 5:
    print("May", year, "has", days[1], "days")
elif month == 6:
    print("June", year, "has", days[1], "days")
elif month == 7:
    print("July", year, "has", days[1], "days")
elif month == 8:
    print("August", year, "has", days[1], "days")
elif month == 9:
    print("September", year, "has", days[1], "days")
elif month == 10:
    print("October", year, "has", days[1], "days")
elif month == 11:
    print("November", year, "has", days[1], "days")
elif month == 12:
    print("December", year, "has", days[1], "days")
