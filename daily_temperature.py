def dailyTemperatures(temperatures):
    if len(temperatures) == 1:
        return [0]
    # create a res variable
    res = []
    # iterate through temperatures
    for i in range(len(temperatures)-1):
        # if curr el is smaller than next el
        if temperatures[i] < temperatures[i+1]:
            # append 1 to the result
            res.append(1)
        # else create a count variable starting at one
        else:
            count = 1
            # create a j variable to loop through the rest of the array
            j = i+1
            # while next el is not greater than curr el
            while j < len(temperatures) and temperatures[j] <= temperatures[i]:
                # increment count
                count += 1
                j += 1
            # append count to the result
            if (j == len(temperatures)):
                res.append(0)
            else:
                res.append(count)
        if i+1 == len(temperatures)-1:
            res.append(0)

    # return result
    return res


# print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))  # [1,1,4,2,1,1,0,0]
# print(dailyTemperatures([30, 40, 50, 60]))  # [1,1,1,0]
# print(dailyTemperatures([30, 60, 90]))  # [1,1,0]
# print(dailyTemperatures([20, 10, 5]))  # [0,0,0]
# [8,1,5,4,3,2,1,1,0,0]
print(dailyTemperatures([89, 62, 70, 58, 47, 47, 46, 76, 100, 70]))
