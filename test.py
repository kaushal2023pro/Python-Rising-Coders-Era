

# While loop in python

# what is while loop?
# -> allows you to repeatedly execute
# a block of code as a specified condition is true



# while True:
    # code to execute repeatedly
#     print("hello world")


# Basic while loop
counter = 0
while counter < 5:
    print("Counter:", counter)
    counter += 1

print()

# Using break statement
counter1 = 0
while True:
    print("Counter:", counter1)
    counter1 += 1
    if counter1 >= 5:
        break

print()

# looping through a list
fruits = ["apple","orange","banana","grape"]
index = 0 
while index < len(fruits):
    print("Fruit:",fruits[index])
    index += 1

# Real-world problem: Counter Timer
# Let's create a countdown timer that takes a 
# user specified time & prints the remaining 
# seconds until the countdown reaches zero.

import time

def countdown_timer(seconds):
    while seconds > 0:
        print("Time remaining", seconds, "seconds")
        time.sleep(1)   #Sleep for 1 second
        seconds -= 1 
    print("Countdown complete!")

# recalling function
countdown_timer(30)

# this program will print the remaining
# seconds until the countdown reaches 0.






