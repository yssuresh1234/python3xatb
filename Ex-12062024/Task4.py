# Fibonaci series
# 0,1,2,3,5,7,9

number = int(input("Enter the number for fibonaci series :\n"))
a = 0
b = 1
print(a)
print(b)
for i in range(1,number):
    c = a + b
    a = b
    b = c
    print(c)
