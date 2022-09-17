class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_num = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hash_num.keys():
                return [hash_num[diff], i]
            hash_num[nums[i]] = i
        