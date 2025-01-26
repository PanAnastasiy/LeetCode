class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        data = {number: nums.count(number) for number in set(nums) if nums.count(number) == 1}
        return sum(data.keys())


print(Solution().sumOfUnique([1, 2, 3, 2]))
