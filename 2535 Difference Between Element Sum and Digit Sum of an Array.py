
class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        digits_sum = sum(list(map(int, list(''.join(map(str, nums))))))
        return abs(sum(nums) - digits_sum)


print(Solution().differenceOfSum([1, 15, 6, 3]))