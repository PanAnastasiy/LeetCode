class Solution(object):
    @staticmethod
    def majorityElement(nums):
        return max(list(filter(lambda x: nums.count(x) > len(nums) / 2, nums)))


print(Solution.majorityElement([2,2,1,1,1,2,2]))