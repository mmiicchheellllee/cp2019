'''
2 (Computing the volume of a cylinder)
C reads in the radius and length of a cylinder and computes its volume using the following formulae:
area = radius * radius * pi
volume = area * length '''

from math import pi

# Get input
radius = float(input("Enter radius: "))
length = float(input("Enter length: "))

# Compute volume
area = radius * radius * pi
volume = area * length

# Output result
print("Volume of cylinder: ""{0:.1f}".format(volume))
