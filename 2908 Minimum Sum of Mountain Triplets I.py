class Solution:
    def minimumSum(self, nums: list[int]) -> int:
        answer = sum(nums)
        flag = False
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] < nums[j] and nums[k] < nums[j]:
                        flag = True
                        answer = min(answer, nums[i] + nums[j] + nums[k])
        return answer if flag else -1


print(Solution().minimumSum([8,6,1,5,3]))