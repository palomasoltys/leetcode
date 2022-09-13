# Given two strings s and t, determine if they are isomorphic.
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

# Example 1:
# Input: s = "egg", t = "add"
# Output: true

# Example 2:
# Input: s = "foo", t = "bar"
# Output: false

def isIsomorphic(s, t):
    if len(s) < 2:                # Quick reject
        return True
    mapping, seen = {}, {}
    for i in range(len(s)):
        if s[i] not in mapping:
            if t[i] in seen:
                return False      # t[i] has already been mapped to, reject
            mapping[s[i]] = t[i]  # Add new mapping
            seen[t[i]] = True     # Keep track of characters already seen in t
        elif mapping[s[i]] != t[i]:
            return False          # Character of s maps to multiple characters in t
    # We found a mapping for all characters without violating the constraints
    return True


print(isIsomorphic("egg", "add"))  # True
print(isIsomorphic("foo", "bar"))  # False
