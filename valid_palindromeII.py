# Given a string s, return true if the s can be palindrome after deleting at most one character from it.

def validPalindrome(s):
    if s[::-1] == s:
        return True
    for i in range(len(s)):
        start = s[:i]
        end = s[i+1:]
        r = start+end
        if r[::-1] == r:
            return True
    return False


print(validPalindrome("abc"))  # false
