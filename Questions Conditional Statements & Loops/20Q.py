#21.Q Write a Python program to check if a number is positive and even using nested if.
num = int(input("Enter a number: "))
if num > 0:
    if num % 2 == 0:
        print("The number is positive and even.")
    else:
        print("The number is positive but not even.")
else:
    print("The number is not positive.")
