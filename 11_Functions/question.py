#1. Write a Python function to sum all the numbers in a list.

def sum (numbers):
    total = 0
    for x in numbers:
     total += x
    return total
print(sum((8, 2, 3, 0, 7)))

#2. Write a Python function to sum all the numbers in a list.
def multiply (numbers):
    total = 1
    for x in numbers:
     total *= x
    return total
print(multiply((8, 2, 3, -1, 7)))

#3. Check whether triangle is valid or not if sides are given
def triangle(a, b, c):
    # check condition
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return False
    else:
        return True
a = int(input("Enter Fast number:"))
b = int(input("Enter Second number:"))
c = int(input("Enter Third number:"))
if triangle(a, b, c):
    print("Valid")
else:
    print("Invalid")
