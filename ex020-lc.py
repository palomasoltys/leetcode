def isValid(s):

    # create an empty dict to keep track of brackets
    # loop through each char in the string
    # if its an open bracket, add 1
    # if its a close bracket, remove 1
    # if value of brackets == 0, return true. otherwise, false

    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}
    for char in s:
        if stack and bracket_map.get(char) == stack[-1]:
            stack.pop()
        else:
            stack.append(char)
    return not stack


print(isValid("({()})"))
