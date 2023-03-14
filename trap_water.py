# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

def trap(height):
    if not height:
        return 0

    n = len(height)
    left_max = [0] * n
    right_max = [0] * n
    left_max[0] = height[0]
    right_max[n-1] = height[n-1]

    # calculate the maximum height seen to the left of each element
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], height[i])

    # calculate the maximum height seen to the right of each element
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], height[i])

    # calculate the amount of water trapped at each element
    trapped_water = 0
    for i in range(n):
        trapped_water += min(left_max[i], right_max[i]) - height[i]

    return trapped_water


print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # 6
print(trap([4, 2, 0, 3, 2, 5]))  # 9
print(trap([4, 2, 3]))  # 1
