#Write a function is_palindrome(s) that returns True if a string is a palindrome, else False.
def is_palindrome(s): #defining the function to check for palindrome
    s = s.lower() #converting the string to lowercase to make the check case-insensitive
    return s == s[::-1] #checking if the string is equal to its reverse
s = str(input("Enter a string: ")) #taking input from the user
print("Is palindrome:", is_palindrome(s)) #printing whether the string is a palindrome or