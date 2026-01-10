"""Write a program that can find area of a triangle.
 It should take base and height as an input from user
and using that it should print an area of a triangle"""
base = int(input("Enter the base of the traingle : "))
height = int(input("Enter the height of the traingle : "))
triangle_area = 0.5 * base * height 
print("Area of triangel is :", triangle_area)
print()

"""Write a program that takes file name with extension as an input 
and prints just the file name without extension
(you can assume that file extensions are always 3 character long)"""
fieName = input("Enter the File name : ").strip()
print(fieName[:-4])