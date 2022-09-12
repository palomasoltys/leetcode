# Given two n x n binary matrices mat and target, return true if it is possible to make mat equal to target by rotating mat in 90-degree increments, or false otherwise.

# Input: mat = [[0,1],[1,0]], target = [[1,0],[0,1]]
# Output: true
# Explanation: We can rotate mat 90 degrees clockwise to make mat equal target.

# Input: mat = [[0,1],[1,1]], target = [[1,0],[0,1]]
# Output: false
# Explanation: It is impossible to make mat equal to target by rotating mat.

def findRotation(mat, target):

    if mat == target:
        return True
    i = 0
    while i <= len(mat):
        for row in range(len(mat)):
            for col in range(row, len(mat)):
                mat[row][col], mat[col][row] = mat[col][row], mat[row][col]
        for r in mat:
            r.reverse()
        if mat == target:
            return True
        i += 1
    return False


# print(findRotation([[0, 1], [1, 0]], [[1, 0], [0, 1]]))  # True
# print(findRotation([[0, 1], [1, 1]], [[1, 0], [0, 1]]))  # False
print(findRotation([[0, 1], [1, 1]], [[0, 1], [1, 1]]))  # True
