#Write a Python program to determine the largest among three given numbers.
numbers = []
# Taking three numbers as input
for i in range(3):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Finding the largest number
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print(f"The largest number is: {largest}")
