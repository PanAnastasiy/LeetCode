class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        print(nums)
        indexes = []
        for i in range(len(nums)):
            if nums[i] == target:
                indexes.append(i)
            elif nums[i] > target:
                return indexes
        return indexes


print(Solution().targetIndices([1, 2, 5, 2, 3], 5))
