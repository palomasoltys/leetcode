# You are given an integer array nums where the largest integer is unique.

# Determine whether the largest element in the array is at least twice as much as every other number in the array. If it is, return the index of the largest element, or return -1 otherwise.

# Input: nums = [3,6,1,0]
# Output: 1
# Explanation: 6 is the largest integer.
# For every other number in the array x, 6 is at least twice as big as x.
# The index of value 6 is 1, so we return 1.

def dominantIndex(nums):
    max_num = max(nums)
    for n in nums:
        if n == max_num:
            continue
        if n * 2 > max_num:
            return -1
    return nums.index(max_num)


print(dominantIndex([3, 6, 1, 0]))  # 1
