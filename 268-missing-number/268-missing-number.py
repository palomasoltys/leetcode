class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        expected_sum = 0 #4     
        for n in nums:
            expected_sum+=n  
            
        real_sum = 0
        for n in range(0, len(nums)+1):
            real_sum+=n
            
        missing = real_sum - expected_sum
        
        if 0 in nums and missing == 0:
            return max(nums) + 1
        elif 0 not in nums and missing == 0:
            return 0
        else:
            return missing