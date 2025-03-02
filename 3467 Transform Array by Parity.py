class Solution:
    def transformArray(self, nums: list[int]) -> list[int]:
        even, odd = 0, 0
        for num in nums:
            if num % 2:
                odd += 1
            else:
                even += 1
        return [0] * even + [1] * odd
