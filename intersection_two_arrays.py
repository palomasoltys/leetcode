# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.

def intersect(nums1, nums2):
    map1 = {}
    map2 = {}
    for num in nums1:
        map1[num] = map1.get(num, 0) + 1
    for num in nums2:
        map2[num] = map2.get(num, 0) + 1
    res = []
    for k, v in map1.items():
        if k in map2:
            if map2[k] == v or map2[k] > v:
                for i in range(v):
                    res.append(k)
            else:
                for i in range(map2[k]):
                    res.append(k)
    return res


print(intersect([4, 9, 5], [9, 4, 9, 8, 4]))  # 4,9 or 9,4
