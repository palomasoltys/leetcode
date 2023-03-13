class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = a[::-1]
        b = b[::-1]
        s = 0
        for i in range(len(a)):
            s += int(a[i]) * 2 ** i
        for i in range(len(b)):
            s += int(b[i]) * 2 ** i
        if s == 0:
            return str(s)
        res = ""  
        while s >= 1:
            res += str(s % 2)
            s = s//2
        return res[::-1]
            
        