class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0

        n = len(obstacleGrid)
        m = len(obstacleGrid[0])

        for i in range(n):
            for j in range(m):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                else:
                    obstacleGrid[i][j] = 1

        for i in range(1, m):
            if obstacleGrid[0][i - 1] == 0:
                obstacleGrid[0][i] = 0

        for i in range(1, n):
            if obstacleGrid[i - 1][0] == 0:
                obstacleGrid[i][0] = 0

        print("+-----------------------------------------")
        for line in obstacleGrid:
            print(line)
        print("+-----------------------------------------")
        for i in range(1, n):
            for j in range(1, m):
                if obstacleGrid[i][j] == 0:
                    continue
                else:
                    obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]
        for line in obstacleGrid:
            print(line)
        return obstacleGrid[-1][-1]


print(Solution().uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
print(Solution().uniquePathsWithObstacles([[0, 1], [0, 0]]))
print(Solution().uniquePathsWithObstacles([[0,1,0,0]]))