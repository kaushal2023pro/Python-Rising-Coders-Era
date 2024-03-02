''' 
------- Source code by `Rising Coders Era`. -------------- 
100+ days python course python course from beginner to advance.
like, share, subscribe. share with your friends.
'lec #3.4' 
'''

fruits = frozenset(["apple","banana","orange"])

for fruit in fruits:
    print(fruit)

# set operations on frozenset
fruits1 = frozenset(["apple","banana","orange"])
fruits2 = frozenset(["banana","grape","kiwi"])

print(type(fruits1))

print("union", fruits1 | fruits2)
print("Intersection", fruits1 & fruits2)
print("difference", fruits1 - fruits2)
print("difference", fruits2 - fruits1)
print("Symmetric difference", fruits1 ^ fruits2)


# dict datatype
# Creating a dictionary of fruits & their quantities
fruits_dict = {
    "apple": 5,
    "banana": 10,
    "orange": 8
}
# modifying the quantity of bananas
fruits_dict["banana"] = 12

# Accessing quantity
print("Quantity of apples", fruits_dict["apple"])
print("Quantity of banana", fruits_dict["banana"])
print("Quantity of orange", fruits_dict["orange"])

# Adding new fruits & its quantity
fruits_dict["grape"] = 15
print("Quantity of grape", fruits_dict["grape"])

# Remove orange entry
del fruits_dict["orange"]
print(fruits_dict)

# iterating through keys
for fruit in fruits_dict:
    print(fruit)

# iterating through values
for quantity in fruits_dict.values():
    print(quantity)

# iterating through key-value pairs
for fruit, quantity in fruits_dict.items():
    print(fruit, quantity)


# checking for the key existency
if "apple" in fruits_dict:
    print("Apple in dict")
else:
    print("not found")


# None datatype
def add(a,b):
    print(a+b)

# calling function
add(2,5)


def greet(name):
    if name is None:
        print("Hello, anonymous user!")
    else:
        print(f"Hello, {name}!")

# calling function with &  without name
greet("Alice")
greet(None)
