class Solution:
    def luckyNumbers(self, matrix: list[list[int]]) -> list[int]:
        answer = []
        for i in range(len(matrix)):
            minimum = min(matrix[i])
            for j in range(len(matrix[i])):
                if matrix[i][j] == minimum and self.checkColumn(minimum, j, matrix):
                    answer.append(minimum)
        return answer

    def checkColumn(self, minimum, index, matrix) -> bool:
        for i in range(len(matrix)):
            if matrix[i][index] > minimum:
                return False
        return True


sol = Solution()
print(sol.luckyNumbers([[3, 7, 8],
                        [9, 11, 13],
                        [15, 16, 17]]))
print(sol.luckyNumbers([[1, 10, 4, 2],
                        [9, 3, 8, 7],
                        [15, 16, 17, 12]]))

