class Solution:
    def judgeCircle(self, moves: str) -> bool:
        col, row = 0, 0
        for move in moves:
            match move:
                case 'U':
                    row += 1
                case 'D':
                    row -= 1
                case 'R':
                    col += 1
                case 'L':
                    col -= 1
        return col == row == 0
