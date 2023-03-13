# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# def two_sum(nums, target):
#     hashmap = {}  # 2:0,
#     for i, el in enumerate(nums):
#         diff = target - el
#         if diff in hashmap.keys():
#             return [hashmap[diff], i]
#         hashmap[el] = i


# print(two_sum([2, 7, 11, 15], 9))  # [0,1]


def buy_stock(prices):
    profit = 0
    l, r = 0, 1
    while r < len(prices):
        if prices[l] < prices[r]:
            profit = max(profit, prices[r] - prices[l])
            r += 1
        else:
            l = r
            r += 1
    return profit


print(buy_stock(
    [1, 2, 4, 2, 5, 7, 2, 4, 9, 0, 9]))  # 9
