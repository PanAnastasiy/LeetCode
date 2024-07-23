from typing import List


class Solution:

    @staticmethod
    def createTargetArray(nums: List[int], index: List[int]) -> List[int]:
        target = []
        for i in range(len(nums)):
            target.insert(index[i], nums[i])
        return target


print(Solution.createTargetArray([0, 1, 2, 3, 4], [0, 1, 2, 2, 1]))