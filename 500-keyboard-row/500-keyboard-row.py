class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        keyb = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        res = []
        p = ""
        w = 0
        r = 0
        k = 0
        while w < len(words):
            while w < len(words) and r < len(words[w]):
                if k >= len(keyb):
                    k = 0
                    w += 1
                while w < len(words) and k < len(keyb) and r < len(words[w]) and words[w][r].lower() in keyb[k] and r <= len(words[w]):
                    p += words[w][r]
                    r += 1
                if w < len(words) and p == words[w]:
                    res.append(p)
                    p = ""
                    k = 0
                    w += 1
                else:
                    p = ""
                    k += 1
                r = 0
        return res