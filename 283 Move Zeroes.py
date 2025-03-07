class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        second_pointer = 0
        for first_pointer in range(len(nums)):
            if nums[first_pointer] != 0:
                nums[second_pointer] = nums[first_pointer]
                second_pointer += 1
        for second_pointer in range(second_pointer, len(nums)):
            nums[second_pointer] = 0


sol = Solution()
print(sol.moveZeroes([0, 1, 0, 3, 12]))
