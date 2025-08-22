class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        return len(set(nums) - {0})


print(Solution().minimumOperations([1, 5, 0, 3, 5]))
