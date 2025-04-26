class Solution:
    def minimumPairRemoval(self, nums: list[int]) -> int:
        answer = 0
        while nums != sorted(nums):
            minimum = sum(nums[:2])
            for i in range(0, len(nums) - 1, 2):
                if sum(nums[i: i + 2]) < minimum:
                    minimum = sum(nums[i: i + 2])
            
