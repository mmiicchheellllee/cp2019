'''
4 (Summing the digits in an integer)
Write a program q4_sum_digits.py that reads an integer between 0 and 1000 and adds all the digits in the integer. For example, if an integer is 932, the sum of all its digits is 14.
Hint: Use the % operator to extract digits, and use the // operator to remove the extracted digit. For instance, 932 % 10 = 2 and 932 // 10 = 93 '''

# Get input
number = int(input("Enter an integer between 0 and 1000: "))

# Compute sum of digits
num = number % 10
rest = number // 10
total = num + rest

# Output result
if number > 0 and number < 1000:
        print("Total sum of digits in integer is: ", total)
        number = False
else:
    if number <= 0 or number >= 1000:
        print("Error input")
