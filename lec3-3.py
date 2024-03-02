''' 
------- Source code by Rising Coders Era. -------------- 
100+ days python course python course from beginner to advance.
like, share, subscribe. share with your friends.
'lec #3.3' 
'''


# Creating a set 
set1 = {1,5,2,3,4,4,5}
# Display the set
print(set1)

# Define String
str = "Rising Coders Era"
# Convert String to a set
char_set = set(str)
# print set of characters
print(char_set)


my_set = set() #empty set
# add single element to set
my_set.add(1)
my_set.add(2)

my_set.update([3,2,1,10])

# Display the updated set
print(my_set)  

# Define set
my_set1 = {1,2,3,4,5}
# Remove element using remove() method
my_set1.remove(3)
# Remove element using discard() method
my_set1.discard(4)
print(my_set1) #Display

# creating 2 sets A & B
A = {1,2,3}
B = {3,4,5}

# union
print("Union", A|B)

# Intersection
print("Intersection", A&B)

# Difference
print("difference", A-B)
print("difference", B-A)

# Symmetric Difference
print("Symmetric Difference", A^B)