#Write a function find_max(a, b, c) that returns the largest of three numbers.
def find_max(a, b, c): #defining the function
    return max(a, b, c) #using built-in max function to find the largest number
a = int(input("Enter first number: ")) #taking input from user
b = int(input("Enter second number: ")) #taking input from user
c = int(input("Enter third number: ")) #taking input from user
print("The largest number is:", find_max(a, b, c)) #printing the largest number
