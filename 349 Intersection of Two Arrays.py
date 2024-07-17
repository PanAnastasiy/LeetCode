from typing import List


class Solution(object):

    @staticmethod
    def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))


print(Solution.intersection([1, 2], [1, 2]))