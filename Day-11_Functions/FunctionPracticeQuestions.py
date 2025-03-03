#WAF to print the length of a list (list is the parameter)
"""
fruits = ["Apple", "Banana", "Mango", "Watermelon", "Papaya", "Grape"]
nums = [1, 3, 5, 4, 8, 9, 2]
def print_len(cal):
    print(len(cal))
print_len(fruits)
print_len(nums)
"""


#3Q Find the sum of all the numbers in a list
"""
# Define a function named 'sum' that takes a list of numbers as input
def sum(numbers):
    # Initialize a variable 'total' to store the sum of numbers, starting at 0
    total = 0
    # Iterate through each element 'x' in the 'numbers' list
    for x in numbers:
        # Add the current element 'x' to the 'total'
        total += x
    # Return the final sum stored in the 'total' variable
    return total
# Print the result of calling the 'sum' function with a tuple of numbers (8, 2, 3, 0, 7)

print(sum((20, 40, 10, 34, 19)))
"""

#factorial number
"""
def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact*=i
    print(fact)
cal_fact(5)
"""
#WAF to convert USD to INR
"""
def convert(usd_dol):
    inr_velu = usd_dol * 87.47
    print(usd_dol, "USD = ", inr_velu, "INR")
convert(1)
"""
#write a program check even or odd
def check(n):
    if n < 2:
        return n % 2 == 0
    return check(n - 2)
n=int(input("Enter number:"))
if check (n) == True:
      print("Number is even!")
else:
      print("Number is odd!")

#Write a Python function to multiply all the numbers in a list. Sample List : (8, 2, 3, -1, 7)
