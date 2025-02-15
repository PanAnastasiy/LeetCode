
class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        dct = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
        if (dct[coordinates[0]] + int(coordinates[1])) % 2:
            return True
        return False


print(Solution().squareIsWhite("a1"))
