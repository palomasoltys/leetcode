def longestCommonPrefix(strs):
    if len(strs) == 1:
        return strs[0]
    prefix = ""
    if strs[0] == "":
        return prefix
    i = 0
    l = 0
    while i <= len(strs) - 2:
        while l < len(strs[i]):
            if strs[i][l] == strs[i+1][l]:
                prefix += strs[i][l]
            else:
                break
            l += 1
        i += 1
    return prefix


print(longestCommonPrefix(["flower", "flow", "flight"]))
