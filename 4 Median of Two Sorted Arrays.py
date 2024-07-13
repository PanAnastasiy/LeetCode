from typing import List


class Solution(object):

    @staticmethod
    def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
        merged = sorted(nums1 + nums2)
        print(merged)
        if len(merged) % 2:
            return merged[len(merged) // 2]
        return (merged[len(merged) // 2] + merged[len(merged) // 2 - 1]) / 2


print(Solution.findMedianSortedArrays([1, 3], [2]))
