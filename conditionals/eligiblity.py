#Write a program that checks if a person is eligible to vote (age ≥ 18).
def eligible(age):
    if age >= 18:
        print(f"wow congrats {name} your'e eligible to participate in elections")
    else:
        print(f"ohh sorry {name} your'e in-eligible to participate in elections")
name = str(input("your good name please: ")).title()
age = int(input("please enter your age: "))
eligible(age)