class Solution:
    def rob(self, nums: list[int]) -> int:
        previous = 0
        current = 0
        for num in nums:
            previous, current = current, max(previous + num, current)
        return current


print(Solution().rob([1, 2, 3, 1]))
print(Solution().rob([2, 7, 9, 3, 1]))
