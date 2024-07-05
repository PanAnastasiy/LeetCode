
class Solution(object):

    @staticmethod
    def removeDuplicates(nums):
        first_pointer = 0
        while first_pointer < len(nums) - 1 and len(nums) > 1:
            second_pointer = first_pointer + 1
            while second_pointer < len(nums) and nums[second_pointer] == nums[first_pointer]:
                del nums[second_pointer]
            first_pointer += 1
        return len(nums)


print(Solution.removeDuplicates([1, 1, 1, 2, 2]))
print(Solution.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
print(Solution.removeDuplicates([1,2,3,4,5,6,6]))
