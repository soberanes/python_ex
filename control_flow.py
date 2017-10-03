#!/usr/bin/env python

# if statement
if True:
    print("Hello Python if")

if 1 > 2:
    print("1 is greater than 2")
elif 2 > 1:
    print("1 is not greater than 2")
else:
    print("1 is equal to 2")


# while statement
num = 1
while num <= 10:
    print(num)
    num += 1

loop_condition = True
while loop_condition:
    print("Loop Condition keeps: %s" %(loop_condition))
    loop_condition = False


# For statement
for i in range(1, 11):
    print(i)
