class Solution:
    def onesMinusZeros(self, grid: list[list[int]]) -> list[list[int]]:
        diff = [[0] * len(grid[0]) for _ in range(len(grid))]
        row_ones = [0] * len(grid)
        row_zeros = [0] * len(grid)
        col_ones = [0] * len(grid[0])
        col_zeros = [0] * len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    row_ones[i] += 1
                    col_ones[j] += 1
                else:
                    row_zeros[i] += 1
                    col_zeros[j] += 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                diff[i][j] = row_ones[i] + col_ones[j] - row_zeros[i] - col_zeros[j]
        return diff


sol = Solution()
print(sol.onesMinusZeros([[0, 1, 1],
                          [1, 0, 1],
                          [0, 0, 1]]
                         ))
