from typing import List


class Solution(object):

    @staticmethod
    def sortedSquares(arr: List[int]) -> List[int]:
        return sorted(list(map(lambda x: x**2, arr)))


print(Solution.sortedSquares([-4, -1, 0, 3, 10]))

