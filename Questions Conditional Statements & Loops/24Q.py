# Print the Fibonacci sequence up to the 10th term using a while loop:
a, b = 0, 1
count = 0
while count < 10:
    print(a, end=" ")
    a, b = b, a + b
    count += 1

#Find the common elements in two lists using a for loop:
list1 = [1, 2, 3, 4, 5, 6, 8]
list2 = [3, 4, 5, 6, 7]
common_elements = []
for i in list1:
    if i in list2 and i not in common_elements:
        common_elements.append(i)
print("Common elements:", common_elements)
