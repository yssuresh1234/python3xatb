# ✅ 2. Triangle Classifier:
# Write a program that classifies a triangle based on its side lengths.
# Given three input values representing the lengths of the sides, determine if the triangle is equilateral (all sides are equal), isosceles (exactly two sides are equal), or scalene (no sides are equal).
# Use an if-else statement to classify the triangle.
# 3 Input
# side 1, side 2 and side 3
# output - Eq, Iso, Scalene -
# Eq. = side 1 == side 2 = side

triangle_side1 = int(input("Enter side 1 of the triangle:\n"))
triangle_side2 =int(input("Enter side 2 of the triangle:\n"))
triangle_side3 = int(input("enter side 3 of the triangle:\n"))

if triangle_side1 == triangle_side2 == triangle_side3:
    print(" Triangle is a Equlateral triangle")
elif triangle_side1 == triangle_side2 != triangle_side3:
    print("Triangle is a isoceles triangle")
elif triangle_side1 != triangle_side2 == triangle_side3:
    print("Triangle is a isoceles triangle")
elif triangle_side1 != triangle_side2 != triangle_side3:
    print("Triangle is a scalene triangle")

