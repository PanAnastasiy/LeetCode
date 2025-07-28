class Solution:
    def deleteGreatestValue(self, grid: list[list[int]]) -> int:
        answer = 0
        for i in range(len(grid)):
            grid[i].sort(reverse=True)
        for j in range(len(grid[0])):
            maxi = -1
            for i in range(len(grid)):
                if grid[i][j] > maxi:
                    maxi = grid[i][j]
            answer += maxi
        return answer


print(Solution().deleteGreatestValue([[1, 2, 4], [3, 3, 1]]))
