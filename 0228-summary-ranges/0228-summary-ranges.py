class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        output = []
        l = 0
        r = 0
        while r < len(nums):
            if r != len(nums) - 1 and nums[r+1] == nums[r] + 1:
                r += 1
            else:
                if l == r:
                    p = f"{nums[r]}"
                else:
                    p = f"{nums[l]}->{nums[r]}"
                output.append(p)
                r += 1
                l = r
        return output