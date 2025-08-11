class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        dct = {}
        for match in matches:
            dct[match[1]] = dct.get(match[1], 0) + 1
            dct[match[0]] = dct.get(match[0], 0)
        win = []
        lose = []
        for pair in dct.items():
            if pair[1] == 1:
                lose.append(pair[0])
            elif pair[1] == 0:
                win.append(pair[0])
        win.sort()
        lose.sort()
        return [win, lose]


print(Solution().findWinners([[1,3], [2,3], [3,6], [5,6], [5, 7],
                              [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]))
