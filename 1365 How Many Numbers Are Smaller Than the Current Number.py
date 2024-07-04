class Solution(object):

    @staticmethod
    def smallerNumbersThanCurrent(nums):
        return [len(list(filter(lambda x: x < nums[first_pointer], nums)))  for first_pointer in range(len(nums))]


print(Solution.smallerNumbersThanCurrent([6, 5, 4, 8]))
