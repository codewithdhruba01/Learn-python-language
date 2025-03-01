"""
def num (a, b): # First input a and b
   return a + b #Return karta he a and b ka sum
   sum = num (1, 2) #sum karke ak variable liya jab hum call function ko call karenge tab a and b ka valu input ke undar jayaga
   print(sum)
"""

"""
# input in function
def num (a, b):
    return a + b
n = int(input("Enter First number:"))
m = int(input("Enter Second number:"))
sum = num (n, m)
print(sum)


#Null Parameter
def name():
    print("Hello World")
name() #call function
name()
name()
"""

"""
#Average of 3 number
def cal_avg(a, b, c):
    sum = a + b + c
    avg = sum/3
    print(avg)
    return avg
cal_avg(21, 58,65)
"""

#defult parameter
def my_function(country = "Norway"):
  print("I am from " + country)
my_function("India")
my_function() #this is Empty Argument



def cal_num(a = 2, b = 5):
    print(a * b)
    return a * b
cal_num()
