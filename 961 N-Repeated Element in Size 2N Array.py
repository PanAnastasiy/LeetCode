class Solution:
    def repeatedNTimes(self, nums: list[int]) -> int:
        unique = set()
        for num in nums:
            if num in unique:
                return num
            else:
                unique.add(num)
        return
