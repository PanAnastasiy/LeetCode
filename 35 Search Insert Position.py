from typing import List


class Solution(object):

    @staticmethod
    def searchInsert(nums: List, target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                return mid
        return left


print(Solution.searchInsert([1, 3, 5, 6], 5))
print(Solution.searchInsert([1, 3, 5, 6], 2))
print(Solution.searchInsert([1, 3, 5, 6], 7))