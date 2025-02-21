from typing import List


class Solution:
    @staticmethod
    def duplicateZeros(arr: list[int]) -> None:
        i = 1
        while i < len(arr):
            if not arr[i - 1]:
                arr.insert(i, 0)
                arr.pop(-1)
                i += 2
            else:
                i += 1


Solution.duplicateZeros([1, 0, 2, 3, 0, 4, 5, 0])
Solution.duplicateZeros([1, 2, 3])