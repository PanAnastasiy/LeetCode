class Spreadsheet:

    def __init__(self, rows: int):
        self.matrix = [[0] * 26 for _ in range(rows)]
        self.dct = {chr(i + 64): i for i in range(1, 27)}

    def setCell(self, cell: str, value: int) -> None:
        column = self.dct[cell[0]] - 1
        row = int(cell[1:]) - 1
        self.matrix[row][column] = value

    def resetCell(self, cell: str) -> None:
        column = self.dct[cell[0]] - 1
        row = int(cell[1:]) - 1
        self.matrix[row][column] = 0

    def getValue(self, formula: str) -> int:
        total = 0
        formula = formula[1:]
        parts = formula.split('+')
        for part in parts:
            if part[0] in self.dct:
                column = self.dct[part[0]] - 1
                row = int(part[1:]) - 1
                total += self.matrix[row][column]
            else:
                total += int(part)
        return total


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
