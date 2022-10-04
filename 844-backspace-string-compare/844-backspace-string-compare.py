class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s = []
        stack_t = []
        for char in s:
            if char == '#' and stack_s:
                stack_s.pop()
            if char != '#':
                stack_s.append(char)
        for char in t:
            if char == '#' and stack_t:
                stack_t.pop()
            if char != '#':
                stack_t.append(char)
        return "".join(stack_s) == "".join(stack_t)
            
        
        