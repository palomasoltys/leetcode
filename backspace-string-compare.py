# Given two strings s and t, return true if they are equal when both are typed into empty text editors.
# '#' means a backspace character.
# Note that after backspacing an empty text, the text will continue empty.

# Input: s = "ab#c", t = "ad#c"
# Output: true
# Explanation: Both s and t become "ac".

def backspaceCompare(s, t):

    def backspace_string(s):
        s_new = []
        for el in s:
            if el == "#":
                if s_new:
                    s_new.pop()
            else:
                s_new.append(el)
        return "".join(s_new)

    return backspace_string(s) == backspace_string(t)


print(backspaceCompare("ab#c", "ad#c"))
