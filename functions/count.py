#Write a function count_vowels(s) that returns the number of vowels in a string.
def count_vowels(s):
    s = s.lower()
    vowels = "aeiou"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

s = str(input("enter a sentence or name?"))
print(count_vowels(s))


    
    