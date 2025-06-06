class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        unique = set()
        not_unique = set()
        for num in nums:
            if num in unique and num not in not_unique:
                unique.remove(num)
                not_unique.add(num)
            if num not in not_unique:
                unique.add(num)
        return unique.pop()


print(Solution().singleNumber([2, 2, 3, 2]))
