class Solution:
    def minOperations(self, nums: list[int]) -> int:
        dct = {0: 1, 1: 0}
        answer = 0
        for i in range(len(nums) - 2):
            if nums[i] == 0:
                nums[i] = dct[nums[i]]
                nums[i + 1] = dct[nums[i + 1]]
                nums[i + 2] = dct[nums[i + 2]]
                answer += 1
        return answer if 0 not in nums else -1


print(Solution().minOperations([0, 1, 1, 1, 0, 0]))
