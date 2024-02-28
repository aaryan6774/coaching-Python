# DOUBTS 10, 14,
# Assignment 5:
# print message 5 times
for i in range(1, 6):
    print("Hello World")

# Question 2:
cnt = 0
for i in range(1, 12):
    print(cnt)
    cnt += 1

# Qustion 3:
print("Even numbers from 1 to 20")
for i in range(1, 20):
    if i % 2==0:
        print(i)

print("Odd numbers from 1 to 20")
for i in range(1,20):
    if i%2 != 0:
        print(i)

# Question 4:
for i in range(1, 20):
    print(i**2)

# Question 5:
sum = 0
for i in range(1, 20):
    sum += i
print("Sum is: ", sum)

# Question 6:
num = int(input("Enter any number to find its table: "))
for i in range(1, 11):
    print(num, "*", i,"=", num*i)

# Question 7:
for i in range(1, 30, 3):
    print(i)

# Question 8:
sum = 0
for i in range(1, 20+1):
    sum+=i
print("Average is: ", sum/20)
print("Even Numbers: ")
for i in range(1, 21):
    if i % 2 == 0:
        print(i)
print("ODD numbers: ")
for i in range(1, 21):
    if i % 2 != 0:
        print(i)

# Question 9:
for i in range(1, 4):
    item_Name = input("Enter item name")
    item_price = int(input("Enter item price"))
    item_quantity = int(input("Enter Quantity"))
    print(item_quantity*item_price)

# Question 10:
max = -1
min = -100
print("enter nums: ")
for i in range(1, 4):
    nums = int(input())
print(max(1, 2, 4, 9, 5, 10))

# Question 10 DOUBT!!!

# Question 11:
for i in range(15, 21):
    print("Cube of ", i, "is", i*i*i)

# Question 12:
import math
for i in range(1, 21):
    print("Square Root of", i, "is", math.sqrt(i))

# Qustion 13:
num = int(input("Enter a number: "))
flag = 0
for i in range(2, num):
    if num % i == 0:
        flag == 0
    else:
        flag == 1

if flag == 1:
    print("Not Prime")
else:
    print("Prime")


# Question 14:  DOUBT!!!
flag = -1
for i in range(15, 26):
    for j in range(2, i):
        if i%j==0:
            flag = 1
        else:
            flag = 0
    continue

if flag == 1:
    print("Not Prime")
else:
    print("Prime")

# Question 15:
