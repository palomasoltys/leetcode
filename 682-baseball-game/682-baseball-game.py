class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for el in operations:
            if el == 'D':
                stack.append(stack[-1]*2)
            elif el == 'C':
                stack.pop()
            elif el == '+':
                s = stack[-1] + stack[-2]
                stack.append(s)
            else:
                stack.append(int(el))
        return sum(stack)