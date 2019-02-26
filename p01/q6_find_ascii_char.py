'''
6 (Finding the character of an ASCII code)
Write a program q6_find_ascii_char.py that receives an ASCII code (an integer between 0 and 127) and displays its character. For example, if the user enters 97, the program displays character a. '''

def ASCII(code):
 return chr(ord(code))
number = int(input("Enter ASCII code: "))
if number < 33:
    print("Enter number from 33 to 127 and number 32 for space")
else:
    print("Character: ", ascii(number))
