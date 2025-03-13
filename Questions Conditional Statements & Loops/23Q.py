#Find the first occurrence of a number in a list using a while loop:
my_list = [3, 8, 2, 7, 4]
target = 7
index = 0
while index < len(my_list):
    if my_list[index] == target:
        break
    index += 1
else:
    index = -1
print(index)