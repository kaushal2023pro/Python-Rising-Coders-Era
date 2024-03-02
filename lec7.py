''' 
------- Source code by Rising Coders Era. -------------- 
 python 100+ days course from beginner to advance.
 lec 7 - while loop.
 like, share, subscribe.
'''

# print number continuously

# i = 0
# while True:
#     print(i)
#     i += 1


# Basic while loop 
# which prints no from 0 to 4

counter = 0
while counter < 5:
    print("Counter: ", counter)
    counter += 1

# break keyword
# "Immediately exits the loop even if"
# "the condition is still true"
    
counter1 = 0
while True:
    print("Counter1: ", counter1)
    counter1 += 1
    if counter1 >= 5:
        break


'''
Continue keyword: "skips the remaining code in the
current iteration & jumps to the next iteration"
'''

# skip even number in while loop

counter3 = 1
while counter3 <= 5:
    if counter3 %2 == 0:
        counter3 += 1
        # skips even no
        continue
    print(f"Current number: {counter3}")
    counter3 += 1

# looping through a list
    
fruits = ["apple","orange","banana","grape"]

index = 0

while index < len(fruits):
    print("fruit: ", fruits[index])
    index += 1


# Real world problem statement
'''
Lets create a countdown timer that takes a
user specified time & prints the 
remaining seconds until the countdown reaches 0.
'''

import time

def countdown_timer(seconds):
    while seconds > 0:
        print("Time remaining", seconds, "seconds")
        time.sleep(5) #sleep for 1 second
        seconds -= 1
    print("Countdown complete!")

# recalling the function
countdown_timer(10)