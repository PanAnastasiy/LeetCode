class Solution:
    def isPossibleToSplit(self, nums: list[int]) -> bool:
        dct = {}
        for num in nums:
            dct[num] = dct.get(num, 0) + 1
            if dct[num] > 2:
                return False
        return True


print(Solution().isPossibleToSplit([1, 1, 2, 2, 3, 4]))
