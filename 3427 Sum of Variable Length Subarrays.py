class Solution:
    def subarraySum(self, nums: list[int]) -> int:
        total = 0
        for i in range(len(nums)):
            total += sum(nums[max(0, i - nums[i]):i+1])
        return total


print(Solution().subarraySum([2, 3, 1]))
print(Solution().subarraySum([3, 1, 1, 2]))
