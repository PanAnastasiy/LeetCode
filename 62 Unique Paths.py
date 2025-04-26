'''
    def uniquePaths(m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        return Solution.uniquePaths(m - 1, n) + Solution.uniquePaths(m, n - 1)
'''


class Solution(object):

    @staticmethod
    def uniquePaths(m: int, n: int) -> int:
        if m == 1 and n == 1:
            return 1
        matrix = [[0 for _ in range(n)] for _ in range(m)]
        matrix[0][1:] = [1] * (n - 1)
        for j in range(1, m):
            matrix[j][0] = 1
        for i in range(1, m):
            for j in range(1, n):
                matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]
        return matrix[-1][-1]


print(Solution.uniquePaths(3, 7))
