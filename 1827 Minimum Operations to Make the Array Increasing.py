class Solution:
    def minOperations(self, nums: list[int]) -> int:
        answer = 0
        check = nums[0]
        for i in range(1, len(nums)):
            if nums[i] <= check:
                check = check + 1
                answer += check - nums[i]
            else:
                check = nums[i]
        return answer


sol = Solution()
print(sol.minOperations([1, 5, 2, 4, 1]))
