#26Q. Write a Python program to determine if a given year is a leap year using nested if.
year = int(input("Enter Year:"))
if year % 4 == 0:
    if year % 100 == 0:
      if year %  400 == 0:
       print(year,"Is a leap year")
      else:
          print(year, "not a leap year")
    else:
          print(year, "is a leap year")
else:
    print(year, "is not a leap year")

#Write a Python program to find the largest of four numbers using nested if.
# Taking input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
num4 = float(input("Enter fourth number: "))

# Using nested if statements to find the largest number
if num1 >= num2:
    if num1 >= num3:
        if num1 >= num4:
            largest = num1
        else:
            largest = num4
    else:
        if num3 >= num4:
            largest = num3
        else:
            largest = num4
else:
    if num2 >= num3:
        if num2 >= num4:
            largest = num2
        else:
            largest = num4
    else:
        if num3 >= num4:
            largest = num3
        else:
            largest = num4

print(f"The largest number is: {largest}")

#this question using loop
numbers = []
for i in range(4):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print(f"The largest number is: {largest}")

