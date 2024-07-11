from typing import List


class Solution(object):

    @staticmethod
    def minimumAverage(nums: List[int]) -> float:
        averages = []
        for _ in range(len(nums) // 2):
            averages.append((min(nums) + max(nums)) / 2)
            nums.remove(max(nums))
            nums.remove(min(nums))
        return min(averages)


print(Solution.minimumAverage([7, 8, 3, 4, 15, 13, 4, 1]))
