#13) Write a Python program to determine whether a person is a
#child (0-12), teenager (13-19), adult (20-59), or senior (60+).
age = int(input("Enter Your Age :"))
if age <= 12:
    print("Child")
elif age <= 19:
    print("Teenager")
elif age <= 59:
    print("Adult")
else:
    print("Senior")

#14) Write a Python program to check whether a number is small
#(less than 10), medium (between 10-100), or large (above 100).

num = int(input("Enter the Number :"))
if num < 10:
    print("small")
elif num < 100:
    print("Medium")
else:
    print("Larges number")