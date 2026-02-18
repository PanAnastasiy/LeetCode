from math import floor


class Solution:
    def averageValue(self, nums: list[int]) -> int:
        total = 0
        counter = 0
        for i in range(len(nums)):
            if nums[i] % 3 == 0:
                total += nums[i]
                counter += 1
        return floor(total / counter) if total else 0
