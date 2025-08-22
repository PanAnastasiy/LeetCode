class Solution:
    def findTheArrayConcVal(self, nums: list[int]) -> int:
        answer = 0
        while len(nums) > 1:
            answer += int(str(nums[0]) + str(nums[-1]))
            nums.pop(0)
            nums.pop(-1)
        return answer if len(nums) == 0 else answer + nums[0]


print(Solution().findTheArrayConcVal([7, 52, 2, 4]))
print(Solution().findTheArrayConcVal([5, 14, 13, 8, 12]))
