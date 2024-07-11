from typing import List


class Solution(object):

    @staticmethod
    def numberOfPairs(nums1: List[int], nums2: List[int], k: int) -> int:
        nums2 = list(map(lambda x: x * k, nums2))
        total = 0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if not nums1[i] % nums2[j]:
                    total += 1
        return total


print(Solution.numberOfPairs([1,2,4,12], [2,4], 3))
