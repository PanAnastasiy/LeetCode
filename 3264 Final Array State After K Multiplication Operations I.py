class Solution:
    def getFinalState(self, nums: list[int], k: int, multiplier: int) -> list[int]:
        for _ in range(k):
            index = nums.index(min(nums))
            nums[index] *= multiplier
        return nums


sol = Solution()
print(sol.getFinalState([2, 1, 3, 5, 6], 5, 2))
