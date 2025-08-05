class Solution:

    def sumOfGoodNumbers(self, nums: list[int], k: int) -> int:
        total = 0
        for i in range(len(nums)):
            left = nums[i - k] if i - k >= 0 else 0
            right = nums[i + k] if i + k < len(nums) else 0
            if left < nums[i] > right:
                total += nums[i]
        return total


print(Solution().sumOfGoodNumbers([1, 3, 2, 1, 5, 4], 2))
print(Solution().sumOfGoodNumbers([2, 1], 1))
