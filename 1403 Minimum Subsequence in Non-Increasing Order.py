class Solution:
    def minSubsequence(self, nums: list[int]) -> list[int]:
        nums.sort(reverse=True)
        for i in range(len(nums)):
            if sum(nums[: i]) > sum(nums[i:]):
                return nums[:i]
        return nums
