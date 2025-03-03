class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        less = []
        eq = []
        greater = []
        for first_pointer in range(len(nums)):
            if nums[first_pointer] < pivot:
                less.append(nums[first_pointer])
            elif nums[first_pointer] == pivot:
                eq.append(nums[first_pointer])
            else:
                greater.append(nums[first_pointer])
        return less + eq + greater


print(Solution().pivotArray([9, 12, 5, 10, 14, 3, 10], 10))
print(Solution().pivotArray([-3, 4, 3, 2], 2))
