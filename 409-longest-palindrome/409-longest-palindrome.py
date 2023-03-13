class Solution:
    def longestPalindrome(self, s: str) -> int:
        maps = {}
        for letter in s:
            maps[letter] = maps.get(letter, 0) + 1
        s = 0
        odd = 0
        for v in maps.values():
            if v % 2 == 0:
                s += v
            else:
                s += v
                odd += 1

        return s if odd <= 1 else s - odd + 1
        
        
        