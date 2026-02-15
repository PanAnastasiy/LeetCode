class Solution:
    def alternatingSum(self, nums: list[int]) -> int:
        return sum([(-1)**i * nums[i] for i in range(len(nums))])
