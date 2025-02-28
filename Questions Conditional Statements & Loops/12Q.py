#12) Write a Python program to assign grades based on marks:
#90-100: A
#80-89: B
#70-79: C
#60-69: D
#Below 60: F

marks = int(input("Enter Your Marks :"))
if marks < 60:
    print(marks,"Fail")
elif (marks>= 60) and (marks <=69):
    print("Your Marks is",marks,"and Your Grade D")
elif(marks >= 70) and (marks <= 79):
    print("Your Marks is", marks, "and Your Grade C")
elif(marks >= 80) and (marks <= 89):
    print("Your Marks is", marks, "and Your Grade B")
elif(marks >= 90) and (marks <= 100):
    print("Your Marks is", marks, "and Your Grade A")
else:
    print("Invalid Number!\nPlese Valid Input")