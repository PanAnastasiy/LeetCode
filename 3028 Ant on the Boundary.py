class Solution:
    def returnToBoundaryCount(self, nums: list[int]) -> int:
        answer = 0
        for i in range(1, len(nums)):
            if sum(nums[: i + 1]) == 0:
                answer += 1
        return answer


print(Solution().returnToBoundaryCount([2, 3, -5]))
print(Solution().returnToBoundaryCount([3, 2, -3, -4]))
