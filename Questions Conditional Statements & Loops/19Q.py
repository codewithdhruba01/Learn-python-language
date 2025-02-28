#Write a Python program to check whether a year is a leap year or not.

year = int(input("Enter Year to Check Leap year or not :"))
if (year % 400 == 0) and (year % 100 == 0):
    print(year, "is a leap year")
elif (year % 4 == 0) and (year % 100!= 0):
    print(year,": is a leap year")
else:
    print(year,"Not a leap year")