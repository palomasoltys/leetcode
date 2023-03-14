# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

# Evaluate the expression. Return an integer that represents the value of the expression.

def evalRPN(tokens):
    if len(tokens) == 1:
        return int(tokens[-1])
    # create a stack
    stack = []
    # iterate through tokens
    for el in tokens:
        # if its a number, add to the stack
        if el.isdigit() or el.lstrip("-").isdigit():
            stack.append(el)
        # else, pop 2 numbers from stack (x and y)
        else:
            if len(stack) > 1:
                x = int(stack.pop())
                y = int(stack.pop())
                # do the math according to the current symbol and add result to the stack
                if el == "+":
                    stack.append(y+x)
                elif el == "-":
                    stack.append(y-x)
                elif el == "/":
                    stack.append(int(y/x))
                elif el == "*":
                    stack.append(y*x)
    # return top of the stack
    return stack[-1]


print(evalRPN(["10", "6", "9", "3", "+", "-11",
      "*", "/", "*", "17", "+", "5", "+"]))  # 22
