class Solution:
    def maximumDifference(self, nums: list[int]) -> int:
        maxi = -1
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i] < nums[j]:
                    maxi = max(nums[j] - nums[i], maxi)
        return maxi
