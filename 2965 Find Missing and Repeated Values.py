
class Solution:
    def findMissingAndRepeatedValues(self, grid: list[list[int]]) -> list[int]:
        keys = [i for i in range(1, len(grid) * len(grid[0]) + 1)]

        answer = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] in keys:
                    keys.remove(grid[i][j])
                else:
                    answer.append(grid[i][j])
        answer.append(keys[0])
        return answer



print(Solution().findMissingAndRepeatedValues([[1, 3], [2, 2]]))
print(Solution().findMissingAndRepeatedValues([[9, 1, 7], [8, 9, 2], [3, 4, 6]]))
