class Solution:
    def tribonacci(self, n: int) -> int:
        arr = [0,1,1]
        f = 0
        s = 1
        t = 2
        while len(arr) < 39:
            arr.append(arr[f]+arr[s]+arr[t])
            f += 1
            s += 1
            t += 1
        return arr[n]
            