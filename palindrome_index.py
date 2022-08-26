def palindromeIndex(s):

    if s == s[::-1]:
        return -1

    l, r = 0, len(s) - 1

    while l < r:
        while s[l] != s[r]:
            p = s[:l]+s[l+1:]
            t = s[:r]+s[r+1:]
            if p == p[::-1]:
                return l
            elif t == t[::-1]:
                return r
            l += 1
            r -= 1
        l += 1
        r -= 1
    return -1


print(palindromeIndex("amorrooma"))
