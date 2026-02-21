class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> list[list[int]]:
        answer = []
        for i in range(rows):
            for j in range(cols):
                answer.append([i, j])
        return sorted(answer, key=lambda x: abs(x[0] - rCenter) + abs(x[1] - cCenter))
