class Solution:
    def minimumArea(self, grid: list[list[int]]) -> int:
        p_row_l, p_column_l = len(grid) - 1, len(grid[0]) - 1
        p_row_f, p_column_f = 0, 0
        rows, cols = set(), set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    rows.add(i)
                    cols.add(j)
        print(rows, cols)
        return (max(rows) - min(rows) + 1) * (max(cols) - min(cols) + 1)


print(Solution().minimumArea([[0,1,0],[1,0,1]]))
print(Solution().minimumArea([[0],[1]]))