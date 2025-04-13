# Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# Output: Maximum subarray sum is 6
# Explanation: [4, -1, 2, 1] has the largest sum = 6

def subarray(nums):
    max_sum = nums[0]
    current_sum = nums[0]
    for n in num[1:]:
        current_sum = max(n, current_sum + n)
        max_sum = max(max_sum,current_sum)
    return max_sum

num = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("maximum subarray sum is ",subarray(num))