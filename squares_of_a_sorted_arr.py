# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

# Example 1:

# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].

def sortedSquares(nums):
    sqr = []
    for n in nums:
        sqr.append(n*n)
    return sorted(sqr)


print(sortedSquares([-4, -1, 0, 3, 10]))  # -> [0,1,9,16,100]
