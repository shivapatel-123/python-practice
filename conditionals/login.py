#Write a program that takes a username and password from the user and checks if they match predefined values (like admin / 1234).
def login(NAME, PASSWORD):
    name = "shiva"
    password = "1234"
    
    if name == NAME and password == PASSWORD:
        print(f"well come {NAME} sir")
    elif name != NAME:
        print("Sir, Please check the name")
    elif password != PASSWORD:
        print("sir, please check the password")
    else:
        print("invalid credentials")
        
NAME = input("User ID: ")
PASSWORD = input("Password: ")

login(NAME, PASSWORD)