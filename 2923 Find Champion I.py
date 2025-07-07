class Solution:
    def findChampion(self, grid: list[list[int]]) -> int:
        for j in range(len(grid)):
            for i in range(len(grid)):
                if grid[i][j] == 1:
                    break
            else:
                return j


print(Solution().findChampion([[0,1],
                                [0,0]]))

print(Solution().findChampion([[0,0,1],
                               [1,0,1],
                               [0,0,0]]))