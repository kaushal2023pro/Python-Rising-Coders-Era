''' 
------- Source code by Rising Coders Era. -------------- 
100+ days python course python course from beginner to advance.
like, share, subscribe. share with your friends.
'lec #3.2' 
'''

# range datatype

# print no from 1-10
my_range = range(1,11)

# printing the elements in the range
for i in my_range:
    print(i)

for i in range(1,6):
    print(i)

# list datatype.
# list of Roll_no.
Roll_no = [100,200,1,30]
print(Roll_no)


# mixed-type list.
mixed_data = ["hello",3.10,500,True]
print(mixed_data)

# list of fruits
fruits = ["apple","banana","strawberry"]
print(fruits)

# accessing elements in a list using index
fruits1 = fruits[0]
print(fruits1)

# modify element in a list
fruits[1] = "orange"
print(fruits)

# adding elements to the end of a list
fruits.append("mango")
print(fruits)

# Remove element from a list
fruits.remove("apple")
print(fruits)

# checking if an element is in a list.
if "orange" in fruits:
    print("orange is in the list!")

# length of list.
length_fruits = len(fruits)
print(length_fruits)

# tuple datatype.
person = ("John",30,"New York")
print(person)

# accessing element using index.
print(person[2])