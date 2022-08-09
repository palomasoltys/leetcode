# The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

# You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

# For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

# Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

# Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
# Output: [-1,3,-1]
# Explanation: The next greater element for each value of nums1 is as follows:
# - 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
# - 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
# - 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.

def next_greater_el(nums1, nums2):
    output = []
    for i in range(len(nums1)):
        if nums1[i] in nums2:
            start = nums2.index(nums1[i])
            end = len(nums2)
            for j in range(start, end):
                if nums1[i] < nums2[j]:
                    output.append(nums2[j])
                    break
                if j == end-1:
                    output.append(-1)

    return output


print(next_greater_el([4, 1, 2], [1, 3, 4, 2]))
