from typing import List


class Solution:

    @staticmethod
    def maxDistance(nums1: List[int], nums2: List[int]) -> int:
        distances = []
        for i in range(len(nums1)):
            for j in range(i, len(nums2)):
                if nums1[i] <= nums2[j]:
                    distances.append((i, j))
        max_distance = max(distances, key=lambda x: x[1] - x[0]) if distances else (0, 0)
        return max_distance[1] - max_distance[0]



print(Solution.maxDistance([5, 4], [3, 2]))
