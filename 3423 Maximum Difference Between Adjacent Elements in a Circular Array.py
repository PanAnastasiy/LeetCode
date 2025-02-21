class Solution:
    def maxAdjacentDistance(self, nums: list[int]) -> int:
        answer = 0
        nums.insert(0, nums[-1])
        nums.insert(len(nums), nums[1])
        for i in range(1, len(nums)):
            if abs(nums[i] - nums[i - 1]) > answer:
                answer = abs(nums[i] - nums[i - 1])
        return answer


print(Solution().maxAdjacentDistance([1, 2, 4]))
print(Solution().maxAdjacentDistance([-5, -10, -5]))
print(Solution().maxAdjacentDistance([-2, 1, -5]))