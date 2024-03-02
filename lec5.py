''' 
------- Source code by Rising Coders Era. -------------- 
 python 100+ days course from beginner to advance.
like, share, subscribe.
'''

'''
    ###  Basic if-elif-else code   ###
'''
if True:
    print("statement 1")
elif True:
    print("statement 2")
elif False:
    print("statement 4")
else:
    print("statement 3")

'''
    ###   PROBLEM STATEMENT - 1   ###
    ->  Write a python program that shows battery level with
        messages like "Full!","Charging", or "Low, charge now!"
    ->  Use if-elif-else to handle full, charging, & low
        (<20%) battery states.
'''

battery_level = int(input("Enter battery level(0-100): "))

if(battery_level >= 80):
    print("Battery is fully charged!")

elif (battery_level >= 50):
    print("Battery is partially charged!")

elif (battery_level >= 20):
    print("Battery is low!")

else:
    print("Battery is low please charge!")


'''
    ###   PROBLEM STATEMENT - 2   ###
    ->  Build a python calculator using if-elif-else
        to handle
        1) Addition
        2) Substraction
        3) Multiplication
        4) Division
        5) Remainder
        6) Square
        7) Cube

    ->  Use clear logic to choose the right 
        operation based on user input.
'''

print("###  Select your choice! ###")

print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")
print("5. Remainder")
print("6. Square")
print("7. Cube")

choice = int(input("Select your choice(1-7): "))
   
a = int(input("Enter 1st no: "))
b = int(input("Enter 2nd no: "))

if choice == 1:
    print("Addition: ", a+b)

elif choice == 2:
    print("Substraction: ", a-b)

elif choice == 3:
    print("Mutiplication: ", a*b)

elif choice == 4:
    print("Division: ", a/b)

elif choice  == 5:
    print("Remainder: ", a%b)

elif choice == 6:
    print("Square of 1st no: ", a**2)
    print("Square of 2nd no: ", b**2)

elif choice == 7:
    print("Cube of 1st no: ", a**3)
    print("Cube of 2nd no: ", b**3)

else:
    print("Choice is invalid, enter between (1-7)")