#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print(f"Last digit of {number}", end=" ")

if (number < 0):
    print(f"is {(-1*((-1*number)%10))}", end=" ")
else:
    print(f"is {number % 10}", end=" ")

if (number % 10 > 5):
    print("and is greater than 5")
elif (number % 10 == 0):
    print("and is 0")
else:
    print("and is less than 6 and not 0")
