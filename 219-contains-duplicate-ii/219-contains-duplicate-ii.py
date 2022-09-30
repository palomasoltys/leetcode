class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_num = {} 
        for i in range(len(nums)):
            if nums[i] in hash_num.keys():
                if abs(i - hash_num[nums[i]]) <= k:
                    return True
            hash_num[nums[i]] = i
        return False