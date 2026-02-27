class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        index = nums.index(max(nums))
        nums.sort()
        return index if nums[-1] >= nums[-2] * 2 else -1