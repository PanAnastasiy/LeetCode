class Solution:
    def minMaxGame(self, nums: list[int]) -> int:
        while len(nums) != 1:
            new_nums = [0] * (len(nums) // 2)
            for i in range(len(new_nums)):
                if i % 2:
                    new_nums[i] = max(nums[i * 2], nums[i * 2 + 1])
                else:
                    new_nums[i] = min(nums[i * 2], nums[i * 2 + 1])
            nums = new_nums
        return nums[0]


print(Solution().minMaxGame([1, 3, 5, 2, 4, 8, 2, 2]))

