from typing import List


class Solution(object):

    @staticmethod
    def countKDifference(nums: List[int], k: int) -> int:
        total = 0
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if abs(nums[i] - nums[j]) == k:
                    total += 1
        return total


print(Solution.countKDifference([3, 2, 1, 5, 4], 2))
