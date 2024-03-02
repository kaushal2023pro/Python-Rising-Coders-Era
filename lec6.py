''' 
------- Source code by Rising Coders Era. -------------- 
 python 100+ days course from beginner to advance.
like, share, subscribe.
'''

'''
EXAMPLE
- TASK1 - write no up to 10.
- TASK2 - now write up to 1000.

USE-
- instead of wrighting code again & again.
    we can use the concepts of loops.
- to perform specific task repeatedly in our program.
- reduces lines of code.
'''

'''
for loop - 
        "To iterate (repeat a block of code)
        over a sequence of elements, such as 
        lists,
        strings,
        tuples or ranges of numbers"
'''

# print no from 0-1000
for i in range(1,1001):
    print(i)

# iterating over a list of names
names = ["Omkar","Sushant","Durgesh"]
for name in names:
    print("Hello, " + name + "!")

# Processing customer orders
orders = [
    {"name": "vivek", "items":["apple","banana"]},
    {"name": "Sahil", "items":["orange","grape"]},
]

for order in orders:
    print("Processing order: ", order["name"])
    print("Items",order["items"])


# Checking for available usernames
usernames = ["Durgesh","Milind","Sanket","Aniket"]
desired_username = input("Enter user name: ")

for username in usernames:
    if username == desired_username:
        print("Username is already taken")
        # Exit a loop when match is found break
        break
    # execute only if the loop completes without a break
else:
    print("Username is not available!")

# Create a multiplication table
table = int(input("Enter no: "))

for i in range(1,21):
    print(table, "x", i, "=", table*i)