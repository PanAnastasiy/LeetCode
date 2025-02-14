
class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        lens = [len(str(num)) for num in nums]
        lens = list(filter(lambda x: not x % 2, lens))
        return len(lens)


print(Solution().findNumbers([12, 345, 2, 6, 7896]))
print(Solution().findNumbers([555, 901, 482, 1771]))
