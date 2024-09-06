class Solution:
    def addedInteger(self, nums1: list[int], nums2: list[int]) -> int:
        return max(nums2) - max(nums1)


sol = Solution()
print(sol.addedInteger([2, 6, 4], [9, 7, 5]))
