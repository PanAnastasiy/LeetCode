from typing import List


class Solution(object):

    @staticmethod
    def isArraySpecial(nums: List[int]) -> bool:
        return all([(nums[i] - nums[i + 1]) % 2 for i in range(len(nums) - 1)])


print(Solution.isArraySpecial([4, 3, 1, 6]))
