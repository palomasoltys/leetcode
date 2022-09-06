# Given a string of lowercase letters in the range ascii[a-z], determine the index of a character that can be removed to make the string a palindrome. There may be more than one solution, but any will do. If the word is already a palindrome or there is no solution, return -1. Otherwise, return the index of a character to remove.

# Example
# Either remove 'b' at index  or 'c' at index .
# Function Description
# Complete the palindromeIndex function in the editor below.
# palindromeIndex has the following parameter(s):
# string s: a string to analyze
# Returns
# int: the index of the character to remove or
# Input Format
# The first line contains an integer , the number of queries.
# Each of the next  lines contains a query string .

# Constraints
# All characters are in the range ascii[a-z].
# Sample Input
# STDIN   Function
# -----   --------
# 3       q = 3
# aaab    s = 'aaab' (first query)
# baa     s = 'baa'  (second query)
# aaa     s = 'aaa'  (third query)
# sadkas

def palindromeIndex(s):

    if s == s[::-1]:
        return -1

    left, right = 0, len(s) - 1

    while left < right:
        while s[left] != s[right]:
            p = s[:left]+s[left+1:]
            t = s[:right]+s[right+1:]
            if p == p[::-1]:
                return left
            elif t == t[::-1]:
                return right
            left += 1
            right -= 1
        left += 1
        right -= 1
    return -1


print(palindromeIndex("amorrooma"))
print(palindromeIndex("sadkas"))  # -> 2 "sakas"
