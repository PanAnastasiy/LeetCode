class Solution:
    def countPoints(self, rings: str) -> int:
        dct = {f'{i}': set() for i in range(0, 10)}
        for i in range(0, len(rings), 2):
            dct[rings[i + 1]].add(rings[i])
        return len(list((filter(lambda x: len(x) == 3, dct.values()))))


print(Solution().countPoints("B0B6G0R6R0R6G9"))
