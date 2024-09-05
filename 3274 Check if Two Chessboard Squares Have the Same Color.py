class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        dict_map = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
        cord1 = (int(dict_map[coordinate1[0]]), int(coordinate1[1]))
        cord2 = (int(dict_map[coordinate2[0]]), int(coordinate2[1]))
        return bool(not (sum(cord1) - sum(cord2)) % 2)


sol = Solution()
print(sol.checkTwoChessboards('a1', 'h3'))
