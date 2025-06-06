class Solution:
    def checkStraightLine(self, coordinates: list[list[int]]) -> bool:
        if len(coordinates) == 2:
            return True
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        if x1 == x2:
            for pair in coordinates[2:]:
                if x1 != pair[0]:
                    return False
            return True
        a = (y1-y2) / (x1 - x2)
        b = y2 - a * x2
        for coordinate in coordinates[2:]:
            if coordinate[1] != a * coordinate[0] + b:
                return False
        return True


print(Solution().checkStraightLine([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]))
print(Solution().checkStraightLine([[0,0],[0,1],[0,-1]]))