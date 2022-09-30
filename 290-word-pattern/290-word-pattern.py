class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(s) != len(pattern):
            return False
        hash_words = {}
        for i in range(len(pattern)):
            if pattern[i] in hash_words.keys() and hash_words[pattern[i]] != s[i]:           
                return False
            if pattern[i] not in hash_words.keys() and s[i] in hash_words.values():
                return False
            hash_words[pattern[i]] = s[i]
        return True