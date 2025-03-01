'''

'''

class Solution:
    def applyOperations(self, nums: list[int]) -> list[int]:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

        first_pointer = 0
        for second_pointer in range(len(nums)):
            if nums[second_pointer]:
                nums[first_pointer] = nums[second_pointer]
                first_pointer += 1

        for i in range(first_pointer, len(nums)):
            nums[i] = 0
        return nums


print(Solution().applyOperations([1, 2, 2, 1, 1, 0]))
print(Solution().applyOperations([0, 1]))
print(Solution().applyOperations([847,847,0,0,0,399,416,416,879,879,206,206,206,272]))
