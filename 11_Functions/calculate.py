# Python program for simple calculator
def addition(num1, num2):
    return num1 + num2
def subtraction(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    return num1 / num2
print("Select Calculation:\n" "1.Addition\n" "2.subtraction\n" "3.multiply\n" "4.divide\n")
a = int(input("Select Operator:"))

n = int(input("Enter first Number:"))
m = int(input("Enter Second Number:"))
if a == 1:
    print(n, "+", m, "=", addition(n, m))
elif a == 2:
    print(n, "-", m, "=", subtraction(n, m))
elif a == 3:
    print(n, "*", m, "=", multiply(n, m))
elif a == 4:
    print(n, "/", m, "=", divide(n, m))
else:
    print("Invalid Input!")