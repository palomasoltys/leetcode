# Given a binary array nums, return the maximum number of consecutive 1's in the array.

# Example 1:

# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

def findMaxConsecutiveOnes(nums):
    ones = 0
    i = 0
    while i < len(nums):
        count = 0
        while i < len(nums) and nums[i] == 1:
            count += 1
            i += 1
        ones = max(ones, count)
        i += 1
    return ones


print(findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))  # 3
