# 1. Explain the difference between the = operator and the ==

#  '=' is an assignment operator and '==' is the comparison operator, both the oprators will return a boolean

# Example :

a = 10
print(a)  # o/p : 10

a = 20
b = 30
print(a == b)  # False

# 2. What does the ** operator do in Python, and how is it used?

# ** operator is used  get a power of a number like a square is written as a**2

number = float(input("Enter a number:"))
number_square = number ** 2
print("Square of the number is :",number_square)

# 3. What does the ^ operator do in Python, and in what context is it commonly used?

# ^ is bitwise xor operation
x = 10  # Binary: 1010
y = 6   # Binary: 0110

result = x ^ y
print(result)  # Output: 12 (Binary: 1100)