from functools import reduce


class Solution:

    def duplicateNumbersXOR(self, nums: list[int]) -> int:
        d = {num: nums.count(num) for num in set(nums) if nums.count(num) > 1}
        twice_numbers = d.keys()
        return reduce(lambda x, y: x ^ y, twice_numbers, 0)


print(Solution().duplicateNumbersXOR([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(Solution().duplicateNumbersXOR([1, 2, 2, 1]))
print(Solution().duplicateNumbersXOR([1, 2, 3]))
