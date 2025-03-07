class Solution:
    def findGCD(self, nums: list[int]) -> int:
        a = min(nums)
        b = max(nums)
        while b:
            a, b = b, a % b
        return a


print(Solution().findGCD([2, 5, 6, 9, 10]))
print(Solution().findGCD([7, 5, 6, 8, 3]))
print(Solution().findGCD([6, 7, 9]))
