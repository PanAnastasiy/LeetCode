class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        return sorted(nums, key=lambda x: nums.count(x))[:2]