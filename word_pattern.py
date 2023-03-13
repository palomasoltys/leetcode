# Given a pattern and a string s, find if s follows the same pattern.
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.
# Example 1:
# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true

def wordPattern(pattern, s):
    s = s.split()
    hash_words = {}
    for i in range(len(pattern)):
        if pattern[i] in hash_words.keys() and hash_words[pattern[i]] != s[i]:
            print(hash_words)
            return False
        hash_words[pattern[i]] = s[i]
    return True


print(wordPattern("abba", "dog cat cat dog"))
