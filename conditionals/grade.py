#Write a program to classify marks: 
#90–100 → Grade A
#75–89 → Grade B
#50–74 → Grade C
#Below 50 → Fail

marks = int(input("Enter marks: "))

if marks >= 90 and marks <= 100:
    print("Grade A")
elif marks >= 75 and marks <= 89:
    print("Grade B")
elif marks >= 50 and marks <= 74:
    print("Grade C")
else:
    print("Fail")
