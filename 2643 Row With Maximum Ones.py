class Solution:
    def rowAndMaximumOnes(self, mat: list[list[int]]) -> list[int]:
        maxi = (0, 0)
        for i in range(len(mat)):
            maxi = max(maxi, (i, mat[i].count(1)), key=lambda x: x[1])
        return maxi
