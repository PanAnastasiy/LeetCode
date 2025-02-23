class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        first_diagonal = 0
        second_diagonal = 0
        col = len(mat[0])
        for i in range(len(mat)):
            first_diagonal += mat[i][i]
            second_diagonal += mat[i][col - i - 1]
        print(first_diagonal)
        print(second_diagonal)
        return first_diagonal + second_diagonal - mat[len(mat) // 2][len(mat[0]) // 2] if len(mat) % 2\
            else first_diagonal + second_diagonal


print(Solution().diagonalSum([[1, 2, 3],
                              [4, 5, 6],
                              [7, 8, 9]]))

print(Solution().diagonalSum([[1,1,1,1],
                                [1,1,1,1],
                                 [1,1,1,1],
                                    [1,1,1,1]]))
