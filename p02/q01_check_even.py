'''
1 (Checking whether a number is even) q01_check_even.py
Write a program that reads an integer and checks whether it is even. 2 sample sessions are as follows:

Enter number: 25
25 is odd

Enter number: 8
8 is even '''

integer = int(input("Enter number: "))
test = integer % 2
if test is 0:
    print(integer, "is even")
elif test is not 0:
    print(integer , "is odd")
