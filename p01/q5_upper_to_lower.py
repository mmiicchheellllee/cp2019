'''
5 (Converting an uppercase letter to lowercase)
Write a program q5_upper_to_lower.py that converts an uppercase letter from standard input to a lowercase letter by making use of its ASCII value. '''

def uppercase_to_lowercase(char):
 return chr(ord(char)+32)
lowercase = input("Uppercase: ")
print("Lowercase: ", uppercase_to_lowercase(lowercase))
