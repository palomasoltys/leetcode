class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}  # 2:0,
        for i, el in enumerate(nums):
            diff = target - el
            if diff in hashmap.keys():
                return [hashmap[diff], i]
            hashmap[el] = i   