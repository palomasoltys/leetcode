class Solution:
    def isValid(self, s: str) -> bool:
        chars = {")":"(",
                 "}":"{",
                 "]":"["}
        stack = []
        for ch in s:
            if stack and chars.get(ch) == stack[-1]:
                stack.pop()
            else:
                stack.append(ch)
        if stack:
            return False
        else:
            return True
        
        
        