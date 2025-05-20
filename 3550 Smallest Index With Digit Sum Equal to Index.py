class Solution:
    def smallestIndex(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            if sum([int(digit) for digit in str(nums[i])]) == i:
                return i
        return -1


print(Solution().smallestIndex([1,2,3,4,5,6,7,8,9]))
