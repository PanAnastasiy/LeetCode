class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        nums.sort(reverse=True)
        for num in nums:
            if -num in nums:
                return num
            if num < 0:
                return -1
        return -1

