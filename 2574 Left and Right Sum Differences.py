
class Solution:
    def leftRightDifference(self, nums: list[int]) -> list[int]:
        leftSum = self.findSum(nums)
        rightSum = self.findSum(nums[::-1])[::-1]
        answer = []
        for i in range(len(nums)):
            answer.append(abs(leftSum[i] - rightSum[i]))
        return answer

    def findSum(self, nums: list[int]) -> list[int]:
        lst = []
        for i in range(len(nums)):
            lst.append(sum(nums[:i]))
        return lst


print(Solution().leftRightDifference([10, 4, 8, 3]))
print(Solution().leftRightDifference([1]))
