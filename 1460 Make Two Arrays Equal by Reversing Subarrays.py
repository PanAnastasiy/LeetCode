from typing import List


class Solution:

    @staticmethod
    def canBeEqual(arr: List[int], target: List[int]) -> bool:
        return sorted(arr) == sorted(target)


print(Solution.canBeEqual([1, 2, 3, 4], [2, 4, 1, 3]))
