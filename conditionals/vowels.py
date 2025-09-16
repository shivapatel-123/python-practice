#Write a program to check if a character entered by the user is a vowel or consonant.

char = input("enter a charater: ")

if char.isalpha():
    if char in "aeiouAEIOU":
        print("it is vowel")
    else:
        print("it is consonent")
else:
        print("it is a number")
        