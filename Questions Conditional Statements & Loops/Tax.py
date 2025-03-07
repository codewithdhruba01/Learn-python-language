# write a program to accept the cost price of a bike and display the road tax to be paid according the criteria--
# >100000 ----- 15% tex
# >50000 and <= 100000 ----- 10% tex
# <=50000 ------- 5% tex

tax = 0
a =  int(input("Enter the cost price of a bike: "))
if a > 100000:
    tax = 15 / 100*a
elif a > 50000 and a <= 100000:
    tax = 10 / 100*a
else:
    tax = 5 / 100*a
print("Road tax to be paid is: ", tax)