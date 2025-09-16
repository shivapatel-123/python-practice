#Write a program to check if a number is even or odd.
def even(n):
    if n % 2 == 0:
        print(f"{n} is a even number")
    else:
        print(f"{n} is a odd number")
    return
n = int(input("enter a number:"))
even(n)