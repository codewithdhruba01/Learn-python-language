#Write a program to find the factorial number-
num = int(input("Enter Number:"))
f = 1
for i in range(1, num+1):
    f = f*i
    print("Factorial is:",f)