#Write a program to check if a number is positive, negative, or zero.

def state(n):
    if n < 0:
        print(f"{n}"+ " " + " is a negative number")
    elif n > 0:
        print(f"{n}"+ " " + "is a positive number")
    else:
        print("given number is zero")

n = int(input("enter a number:"))
state(n)
    