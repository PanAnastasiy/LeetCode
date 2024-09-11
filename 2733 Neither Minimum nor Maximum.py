class Solution:
    def findNonMinOrMax(self, nums: list[int]) -> int:
        return sorted(nums)[1] if len(nums) > 2 else -1
