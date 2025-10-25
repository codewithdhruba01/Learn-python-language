# Find maximum element in a list using recursion.

def max_recursive(lst):
    # Base case: agar list me sirf ek element hai, wahi max hoga
    if len(lst) == 1:
        return lst[0]
    
    # Recursive case: first element aur baki list ka max compare karo
    sub_max = max_recursive(lst[1:])
    return lst[0] if lst[0] > sub_max else sub_max

# Example
numbers = [5, 2, 9, 1, 7]
print("Maximum element:", max_recursive(numbers))
