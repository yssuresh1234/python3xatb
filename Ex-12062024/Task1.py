# Leap Year checker
# Create a program that determines whether a given year is a leap year.
# A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.
# Use an if-else statement to make this determination.
# Input = 2024
# Output = Leap

year_input = int(input("Enter Year (YYYY):"))
leap_year = year_input % 4
end_of_cf_centuary_year = year_input % 400 and year_input % 100

if leap_year == 0:
    print(year_input, "is the leap year")
elif end_of_cf_centuary_year == 0:
    print(year_input,"is the leap centuary")
else:
    print("not a leap year")


