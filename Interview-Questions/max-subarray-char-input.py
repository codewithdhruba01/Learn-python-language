"""
Sample Input:
Enter numbers for array
Enter x to stop
Enter a number 1
Enter a number -2
Enter a number 3
Enter a number 5
Enter a number -1
Enter a number x

Sample Output:
Maximum subarray sum = 8
"""


def get_list() -> list[int]:
    print("Enter numbers for array \nEnter x to stop")
    numbers = []
    entry = input("Enter a number: ")
    while entry.lower() != "x":
        numbers.append(int(entry))
        entry = input("Enter a number: ")
    return numbers


def max_subarray(arr: list[int]) -> int:
    max_sum = float("-inf")
    current_sum = 0
    if not arr:
        return 0
    for num in arr:
        current_sum += num
        max_sum = max(max_sum, current_sum)
        if current_sum < 0:
            current_sum = 0
    return max_sum


arr = get_list()
print(f"Maximum subarray sum = {max_subarray(arr)}")
