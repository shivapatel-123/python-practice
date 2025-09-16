#Write a program to check if a given year is a leap year.
#(Hint: divisible by 4 but not by 100, unless divisible by 400).

year = int(input("Enter Year:"))

if (year % 400 == 0):
    print(f"{year} is a leap year")
elif (year % 100 == 0):
    print(f"{year} is not a leap year")
elif (year % 4 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
        
    