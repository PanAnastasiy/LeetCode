class Solution(object):

    '''
    def majorityElement(self, nums: List[int]) -> int:
     return max(list(filter(lambda x: nums.count(x) > len(nums) / 2, nums)))
    '''


    @staticmethod
    def majorityElement(nums):
        dct = {num: nums.count(num) for num in set(nums)}
        return max(dct, key=dct.get)


print(Solution.majorityElement([2, 2, 1, 1, 1, 2, 2]))
print(Solution.majorityElement([2, 2, 1, 1, 1, 2, 2, 2, 2]))