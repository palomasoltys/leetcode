# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

def generateParenthesis(n):
    stack = []
    res = []

    def backtrack(openN, closeN):
        if openN == closeN == n:
            res.append("".join(stack))

        if openN < n:
            stack.append("(")
            backtrack(openN + 1, closeN)
            stack.pop()
        if closeN < openN:
            stack.append(")")
            backtrack(openN, closeN + 1)
            stack.pop()

    backtrack(0, 0)
    return res


print(generateParenthesis(3))
