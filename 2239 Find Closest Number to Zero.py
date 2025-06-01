class Solution:
    def findClosestNumber(self, nums: list[int]) -> int:
        number = min(nums, key=lambda x: abs(x))
        return -number if number < 0 and -number in nums else number
