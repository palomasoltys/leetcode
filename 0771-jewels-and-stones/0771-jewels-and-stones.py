class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        s = {}
        count = 0
        for stone in stones:
            s[stone] = s.get(stone, 0) + 1
        for j in jewels:
            if j in s:
                count += s[j]
        return count