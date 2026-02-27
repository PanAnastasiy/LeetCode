class Solution:
    def constructTransformedArray(self, nums: list[int]) -> list[int]:
        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                value = nums[(i + nums[i]) % len(nums)]
            elif nums[i] < 0:
                value = nums[(i + len(nums) + nums[i]) % len(nums)]
            else:
                value = nums[i]
            result.append(value)
        return result
