class Solution:
    def dominantIndices(self, nums: list[int]) -> int:
        counter = 0
        n = len(nums)
        total = sum(nums[1:])
        for i in range(n - 1):
            if nums[i] > total / (n - i - 1):
                counter += 1
            total -= nums[i]
        return counter

