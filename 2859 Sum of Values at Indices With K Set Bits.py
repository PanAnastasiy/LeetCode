class Solution:
    def sumIndicesWithKSetBits(self, nums: list[int], k: int) -> int:
        total = 0
        for i in range(len(nums)):
            if bin(i).count('1') == k:
                total += nums[i]
        return total


print(Solution().sumIndicesWithKSetBits([5, 10, 1, 5, 2], 1))