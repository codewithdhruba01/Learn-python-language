#Find the average of numbers in a list using a for loop:
my_list = [4, 7, 9, 2, 5]
total = 0
for num in my_list:
    total += num
average = total / len(my_list)
print(average, "average numbers")

#Find the largest number in a list using a for loop:

my_list = [3, 19, 19, 60, 28, 80]
largest = my_list[0]
for i in my_list:
    if i > largest:
        largest = i
print(largest, "is a largest Number")