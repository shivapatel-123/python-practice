#Write a program to calculate electricity bill:
#First 100 units → ₹1.5/unit
#Next 100 units → ₹2.5/unit
#Above 200 units → ₹4/unit

def current(units):
    if units <= 100:
        return 1.5 * units 
    if units >= 100:
        return 2.5 * units
    if units >= 200:
        return 4 * units

units = int(input("enter units: "))
print(f"your bill is :{current(units)} rupees")


#chatgpt code

def current(units):
    if units <= 100:
        bill = units * 1.5
    elif units <= 200:            # 101 to 200 units
        bill = 100 * 1.5 + (units - 100) * 2.5
    else:                          # above 200 units
        bill = 100 * 1.5 + 100 * 2.5 + (units - 200) * 4
    return bill

units = int(input("Enter units: "))
print(f"Your bill is: {current(units)} rupees")


        