# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.
# Example 1:
# Input: nums = [2,2,1]
# Output: 1

def singleNumber(nums):
    seen = set()
    for n in nums:
        if n in seen:
            seen.remove(n)
        else:
            seen.add(n)
    return seen.pop()


print(singleNumber([2, 2, 1]))  # -> 1
