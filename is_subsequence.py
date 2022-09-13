# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

# Example 1:
# Input: s = "abc", t = "ahbgdc"
# Output: true

# Example 2:
# Input: s = "axc", t = "ahbgdc"
# Output: false

def isSubsequence(s, t):
    l = 0
    r = 0
    p = ""
    while l < len(s) and r < len(t):
        if s[l] == t[r]:
            p += s[l]
            l += 1
        r += 1
    if p == s:
        return True
    else:
        return False


print(isSubsequence("abc", "ahbgdc"))  # True
print(isSubsequence("axc", "ahbgdc"))  # False
