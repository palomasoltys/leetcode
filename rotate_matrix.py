# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]

def rotate(matrix):
    # transpose
    for row in range(len(matrix)):
        for col in range(row, len(matrix)):
            matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
    # reverse
    for row in matrix:
        row.reverse()
    return matrix


print(rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))  # [[7,4,1],[8,5,2],[9,6,3]]
