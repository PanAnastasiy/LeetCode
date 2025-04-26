class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    continue
                if i == 0 and j != 0:
                    grid[0][j] = grid[0][j] + grid[0][j - 1]
                elif j == 0 and i != 0:
                    grid[i][0] = grid[i][0] + grid[i - 1][0]
                else:
                    grid[i][j] = grid[i][j] + min(grid[i - 1][j], grid[i][j - 1])
        return grid[-1][-1]


print(Solution().minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
print(Solution().minPathSum([[1, 2, 3], [4, 5, 6]]))
