class Solution:
    def sumOfSquares(self, nums: list[int]) -> int:
        answer = []
        n = len(nums)
        for i in range(n):
            if n % (i + 1) == 0:
                answer.append(nums[i] ** 2)
        return sum(answer)
