def generate(numRows):
    output = [[1], [1, 1]]
    l, r = 0, 0
    res = []
    while len(output) != numRows:
        if l == r or l == len(output[-1]) - 1:
            res.append(output[-1][l])
        else:
            res.append((output[-1][l] + output[-1][r]))
        if l == len(output[-1])-1:
            output.append(res)
            res = []
            l, r = 0, 0
        if l == r and len(res) > 0:
            r += 1
        elif l != r and len(res) > 0:
            r += 1
            l += 1
    return output


print(generate(5))
