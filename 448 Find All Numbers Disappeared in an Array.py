class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        data = dict.fromkeys(list(range(1, len(nums) + 1)), 0)
        for num in set(nums):
            data[num] += 1
        return list(filter(lambda x: not data[x], data))



sol = Solution()
print(sol.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
print(sol.findDisappearedNumbers([1, 1]))