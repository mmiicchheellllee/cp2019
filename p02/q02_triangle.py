'''
2 (Validating triangles and computing perimeter) q02_triangle.py
Write a program that reads three edges for a triangle and determines whether the input is valid. The input is valid if the sum of any two edges is
greater than the third edge. The program will compute the perimeter of the triangle if the input is valid. Otherwise, display that the input is
invalid. 2 sample sessions are as follows:

Enter side 1: 2
Enter side 2: 2
Enter side 3: 1
Perimeter = 5

Enter side 1: 1
Enter side 2: 2
Enter side 3: 1
Invalid triangle! '''

side_1 = float(input("Enter side 1: "))
side_2 = float(input("Enter side 2: "))
side_3 = float(input("Enter side 3: "))
perimeter = side_1 + side_2 + side_3
if side_1 + side_2 <= side_3:
    print("Invalid triangle!")
elif side_1 + side_3 <= side_2:
    print("Invalid triangle!")
elif side_2 + side_3 <= side_1:
    print("Invalid triangle!")
else:
    print("Perimeter = ""{0:.0f}".format(perimeter))
