''' 
------- Source code by Rising Coders Era. -------------- 
100+ days python course python course from beginner to advance.
like, share, subscribe. share with your friends.
'lec #3.1' 
'''

# length function

a = len("this is length")
b = len("hello")
print(a+b)

# e = len("100")
# print(e)

# bytes - datatype
# 65 = A
# 66 = B
# 67 = C
# 68 = D
my_bytes = bytes([65,66,67])
print(my_bytes)
print(len(my_bytes))
print(type(my_bytes))

# bytearray datatype
my_bytearray = bytearray([65,66,67])
my_bytearray[1] = 68
print(my_bytearray)
print(type(my_bytearray))