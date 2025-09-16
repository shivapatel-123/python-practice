# Write a function reverse_string(s) that returns the reversed version of the string.
def reverse_string(s): #defining the function to reverse the string
    return s[::-1] #using slicing to reverse the string
s = str(input("Enter a string: ")) #taking input from the user
print("Reversed string:", reverse_string(s)) #printing the reversed string
