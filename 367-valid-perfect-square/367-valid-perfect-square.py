class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        sqr = round(num ** (1/2))
        return sqr * sqr == num
        