class Solution:
    def minElement(self, nums: list[int]) -> int:
        return min([self.findSumOfDigits(num) for num in nums])

    def findSumOfDigits(self, num: int) -> int:
        print(sum(list(map(int, str(num)))))
        return sum(list(map(int, str(num))))


print(Solution().minElement([10,11,12,13,14,15]))
