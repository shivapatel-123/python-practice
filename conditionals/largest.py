#Write a program to find the largest of two numbers entered by the user.
def largest(a, b):
    if a > b:
        print(f"{a} is largest number ")
    else:
        print(f"{b} is largest number ")
a = int(input("what's a:"))
b = int(input("what's b:"))

largest(a, b)