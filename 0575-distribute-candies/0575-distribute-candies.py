class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        c = {}
        for candy in candyType:
            c[candy] = c.get(candy, 0) + 1
        n = len(candyType) / 2
        if n >= len(c):
            return len(c)
        else:
            return int(n)
        
        