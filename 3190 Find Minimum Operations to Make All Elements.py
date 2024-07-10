from typing import List


class Solution(object):

    @staticmethod
    def minimumOperations(nums: List[int]) -> int:
        counter = 0
        for num in nums:
            if num % 3:
                counter += 1
        return counter


print(Solution.minimumOperations([3, 6, 9]))
