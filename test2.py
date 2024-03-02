# Nested loop
'''
'loop inside another loop'. This allows 
you to iterate over elements in a 
more complex way.
'''

'''
Nested for loops:
->  Using multiple `for` loops 
    inside each other.
'''

# for i in range(3):
#     for j in range(2):
#         print(i,j)


'''
Nested while loops:
->  Similar to nested `for` loops but
    using `while` statements.
'''

# i = 0
# while i < 3:
#     j = 0
#     while j < 2:
#         print(i,j)
#         j += 1
#     i += 1

'''
Nested loop with control statement
->  using break / continue statemets 
    within nested loops for more control.
'''

for i in range(3):
    for j in range(2):
        if i == j:
            break
        print(i,j)