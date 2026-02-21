class Solution:
    def isGood(self, nums: list[int]) -> bool:
        nums.sort()
        max_value = nums[-1]
        based = list(range(1, max_value)) + [max_value, max_value]
        print(based)
        return nums == based


print(Solution().isGood([1, 3, 3, 2]))