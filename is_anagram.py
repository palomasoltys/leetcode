# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

def isAnagram(s, t):

    if len(s) != len(t):
        return False

    s_dict = {}
    t_dict = {}

    for i in range(len(s)):
        s_dict[s[i]] = s_dict.get(s[i], 0) + 1
        t_dict[t[i]] = t_dict.get(t[i], 0) + 1

    if s_dict == t_dict:
        return True
    else:
        return False


print(isAnagram("anagram", "nagaram"))
