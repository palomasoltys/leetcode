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
