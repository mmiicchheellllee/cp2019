'''
3 (Converting miles into kilometers)
Write a program q3_miles_to_kilometre.py that reads a number in miles, converts it to kilometres, and displays the result. One mile is 1.60934 kilometres. Display your answer correct to 3 decimal places. '''

# Get input
Miles = float(input("Enter distance in miles: "))

# Compute distance in Kilometres
Kilometres = 1 * 1.60934

# Output result
print("Distance in Kilometres: ""{0:.3f}".format(Kilometres))
