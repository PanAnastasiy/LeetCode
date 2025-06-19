class Solution:
    def checkValid(self, matrix: list[list[int]]) -> bool:
        for i in range(len(matrix)):
            row = set()
            column = set()
            for j in range(len(matrix)):
                if matrix[i][j] in row or matrix[j][i] in column:
                    return False
                else:
                    row.add(matrix[i][j])
                    column.add(matrix[j][i])
        return True


print(Solution().checkValid([[1, 2, 3], [3, 1, 2], [2, 3, 1]]))

