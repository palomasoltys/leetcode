class Solution:
    def isHappy(self, n: int) -> bool:
        track = set()
        while n != 1:
            n = str(n)
            soma = 0
            for num in n:
                soma += int(num) ** 2
            n = soma
            if n in track:
                return False
            track.add(n)            
        return True