class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        i = set(nums1) & set(nums2)
        return min(i) if i else -1
