class Solution:
    def minimumPairRemoval(self, nums: list[int]) -> int:
        answer = 0
        while nums != sorted(nums):
            minimum = nums[0] + nums[1]
            index = 0
            for i in range(len(nums) - 1):
                if nums[i] + nums[i + 1] < minimum:
                    minimum = nums[i] + nums[i + 1]
                    index = i
            nums[index] = minimum
            nums.pop(index + 1)
            answer += 1
        return answer
            

print(Solution().minimumPairRemoval([5,2,3,1]))
