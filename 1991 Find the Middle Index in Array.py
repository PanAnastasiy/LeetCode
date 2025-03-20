class Solution:
    def findMiddleIndex(self, nums: list[int]) -> int:
        index = -1
        for i in range(len(nums)):
            if sum(nums[:i]) == sum(nums[i+1:]):
                return i
        return index


print(Solution().findMiddleIndex([2, 3, -1, 8, 4]))
print(Solution().findMiddleIndex([1, -1, 4]))
