class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        answer = 0
        nums.sort()
        for i in range(0, len(nums), 2):
            answer += nums[i]
        return answer
