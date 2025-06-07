class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        decrease = False
        increase = False
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            if nums[i] < nums[i-1] and not increase:
                decrease = True
            elif nums[i] > nums[i - 1] and not decrease:
                increase = True
            else:
                return False
        return True
