'''
6 (Conversion from kilograms to pounds) q06_kilograms_to_pounds.py
Write a program that displays the following table (1 kilogram = 2.2 pounds):

Kilograms Pounds
1         2.2
2         4.4
3         6.6
...
9         19.8
10        22.0 '''

print("Kilograms", "Pounds")
for i in range(1,11):
    print("{0:<10}{1:.1f}".format(i, i * 2.2))
