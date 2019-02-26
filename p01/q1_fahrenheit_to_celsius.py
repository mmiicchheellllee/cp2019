'''
1. (Converting Fahrenheit to Celsius)
Write a program q1_fahrenheit_to_celsius.py that reads a Fahrenheit degree in double (floating point / decimal) from standard input, then converts it to Celsius and displays the result in standard output. The formula for the conversion is as follows: celsius = (5/9) * (fahrenheit - 32)'''

# Get input
fahrenheit = int(input("Enter temperature in Fahrenheit: "))

# Compute celsius temperature
celsius = (5/9) * (fahrenheit - 32)

# Output result
print("Temperature in Celsius: ""{0:.1f}".format(celsius))
