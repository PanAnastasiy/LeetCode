import numpy as np


class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        answer = np.transpose(matrix)
        return answer.tolist()


print(Solution().transpose([[1, 2, 3],
                            [4, 5, 6],
                            [7, 8, 9]]))
