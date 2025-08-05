from itertools import zip_longest


class Solution:
    def sortEvenOdd(self, nums: list[int]) -> list[int]:
        odd_nums = []
        even_nums = []
        for i in range(len(nums)):
            if i % 2:
                odd_nums.append(nums[i])
            else:
                even_nums.append(nums[i])
        odd_nums.sort(reverse=True)
        even_nums.sort()
        return [number for pair in zip_longest(even_nums, odd_nums) for number in pair if number is not None]


print(Solution().sortEvenOdd([4, 1, 2, 3]))
