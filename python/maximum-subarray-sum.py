# Function finds the largest sum of any contiguous subarray using Kadane's algorithm
# Input: list of numbers
# Output: int
# Runtime Complexity: O(n), Space Complexcity: O(1)
def max_subarray_sum(numbers: list[int]) -> int:
    if len(numbers) == 0:
        raise(ValueError("Empty array provided"))
    best_sum = float('-inf')
    current_sum = 0
    for x in numbers:
        current_sum = max(x, current_sum + x)
        best_sum = max(best_sum, current_sum)
    return best_sum

def test(input=[-2, 1, -3, 4, -1, 2, 1, -5, 4]): # Default value
    output = max_subarray_sum(input)
    print(f"Input: {input} => Maximum subarray sum: {output}")

def sample1():
    """
    Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    Output: Maximum subarray sum is 6
    Explanation: [4, -1, 2, 1] has the largest sum = 6
    """
    test([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    

def sample2():
    """
    Input: [-1, -2, -1]
    Output: Maximum subarray sum is -1
    Explanation: [-1] has the largest sum = -1
    """
    test([-1, -2, -1])

def sample3():
    """
    Input: [1, 2, -3, 4, 5]
    Output: Maximum subarray sum is 9
    Explanation: [4, 5] has the largest sum = 9
    """
    test([1, 2, -3, 4, 5])

if __name__ == "__main__":
    #sample1()
    #sample2()
    #sample3()
    pass
