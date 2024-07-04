
class Solution(object):

    @staticmethod
    def removeDuplicates(nums):
        first_pointer = 0
        for first_pointer in range(len(nums)):
            second_pointer = first_pointer + 1
            while nums[first_pointer] == nums[second_pointer]:
                del nums[second_pointer]
                second_pointer += 1


print(Solution.removeDuplicates([1, 1, 1, 2]))
