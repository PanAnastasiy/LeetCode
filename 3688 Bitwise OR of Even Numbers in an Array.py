class Solution:
    def evenNumberBitwiseORs(self, nums: list[int]) -> int:
        result = 0
        for num in nums:
            if not num % 2:
                result |= num
        return result
