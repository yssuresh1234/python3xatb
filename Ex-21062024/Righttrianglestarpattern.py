number_of_patterns=int(input("Enter number of pattern to be printed :\n"))

for i in range(1,number_of_patterns + 1):
    for j in range(i):
        print('*',end='')
    print()

