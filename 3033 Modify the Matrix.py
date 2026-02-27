from typing import List


class Solution:

    def find_max_in_column(self, matrix: List[List[int]], j) -> int:
        result = matrix[0][j]
        for i in range(1, len(matrix)):
            result = max(result, matrix[i][j])
        return result

    def modifiedMatrix(self, matrix: list[list[int]]) -> list[list[int]]:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == -1:
                    matrix[i][j] = self.find_max_in_column(matrix, j)
        return matrix
