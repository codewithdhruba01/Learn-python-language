"""
Sample Input:
Enter numbers for array
Enter x to stop
Enter a number 1
Enter a number 2
Enter a number 3
Enter a number 5
Enter a number 1
Enter a number x

Sample Output:
Maximum subarray sum = 12
"""

def get_list() -> list[str]:
    print("Enter numbers for array \nEnter x to stop")
    numbers = []
    while True:
        entry = input("Enter a number: ")
        if entry.lower() == "x":
            break
        if not entry.isnumeric():
            print("Input must only be a non-negative integer")
            continue
        numbers.append(entry)
    return numbers


def max_subarray(arr: list[str]) -> int:
    max_sum = float("-inf")
    current_sum = 0
    arr_int = list(map(int, arr))
    if not arr_int:
        return 0
    for num in arr_int:
        current_sum += num
        max_sum = max(max_sum, current_sum)
        if current_sum < 0:
            current_sum = 0
    return max_sum


arr = get_list()
print(f"Maximum subarray sum = {max_subarray(arr)}")
