def dailyTemperatures(temperatures):
    res = [0] * len(temperatures)
    stack = []  # pair: [temp, index]

    for i, t in enumerate(temperatures):
        while stack and t > stack[-1][0]:
            stackT, stackInd = stack.pop()
            res[stackInd] = i - stackInd
        stack.append((t, i))
    return res


print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))  # [1,1,4,2,1,1,0,0]
print(dailyTemperatures([30, 40, 50, 60]))  # [1,1,1,0]
print(dailyTemperatures([30, 60, 90]))  # [1,1,0]
print(dailyTemperatures([20, 10, 5]))  # [0,0,0]
# [8,1,5,4,3,2,1,1,0,0]
print(dailyTemperatures([89, 62, 70, 58, 47, 47, 46, 76, 100, 70]))
