# You are keeping score for a baseball game with strange rules. The game consists of several rounds, where the scores of past rounds may affect future rounds' scores.

# At the beginning of the game, you start with an empty record. You are given a list of strings ops, where ops[i] is the ith operation you must apply to the record and is one of the following:

# An integer x - Record a new score of x.
# "+" - Record a new score that is the sum of the previous two scores. It is guaranteed there will always be two previous scores.
# "D" - Record a new score that is double the previous score. It is guaranteed there will always be a previous score.
# "C" - Invalidate the previous score, removing it from the record. It is guaranteed there will always be a previous score.
# Return the sum of all the scores on the record. The test cases are generated so that the answer fits in a 32-bit integer.

# Input: ops = ["5","2","C","D","+"]
# Output: 30

def calPoints(ops):

    score = []
    for i in range(len(ops)):
        if ops[i] == "C":
            score.pop()
        elif ops[i] == "D":
            score.append(score[-1]*2)
        elif ops[i] == "+":
            score.append(score[-2] + score[-1])
        else:
            score.append(int(ops[i]))
    return sum(score)


print(calPoints(["5", "2", "C", "D", "+"]))  # -> 30
